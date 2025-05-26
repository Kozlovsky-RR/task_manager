"""Файл конфигураций для работы с тестами."""

import asyncio

import pytest
from sqlalchemy import insert

from app.config import settings
import json
from app.database import Model, new_session, engine
from app.models.tasks_models import TaskOrm
from app.models.users_models import UserOrm

from httpx import AsyncClient, ASGITransport
from app.main import app as fastapi_app


@pytest.fixture(scope="function", autouse=True)
async def prepare_db():
    """Подключение к тестовой бд."""
    if settings.MODE == "TEST":
        async with engine.begin() as conn:
            await conn.run_sync(Model.metadata.drop_all)
            await conn.run_sync(Model.metadata.create_all)

        def open_mock_json(model: str):
            with open(
                f"app/tests/mock_{model}.json", encoding="utf-8", mode="r"
            ) as file:
                return json.load(file)

        users = open_mock_json("users")
        tasks = open_mock_json("tasks")

        for i in users:
            i.update(password=bytes(i.get("password"), "utf-8"))

        async with new_session() as session:
            """Наполнение данными тестовой бд"""
            add_users = insert(UserOrm).values(users)
            add_tasks = insert(TaskOrm).values(tasks)

            await session.execute(add_users)
            await session.execute(add_tasks)

            await session.commit()


@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def ac():
    """Не аутентифицированный тестовый пользователь."""
    async with AsyncClient(
        transport=ASGITransport(app=fastapi_app), base_url="http://test"
    ) as ac:
        yield ac


@pytest.fixture(scope="session")
async def authenticated_ac():
    """Аутентифицированный тестовый пользователь."""
    async with AsyncClient(
        transport=ASGITransport(app=fastapi_app), base_url="http://test"
    ) as ac:
        auth = await ac.post(
            "/auth/login/",
            data={"username": "rus@gmail.com", "password": "12345"},
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        assert auth.status_code == 200, f"Login failed: {auth.text}"
        token = auth.json()["access_token"]
        ac.headers.update({"Authorization": f"Bearer {token}"})
        yield ac
