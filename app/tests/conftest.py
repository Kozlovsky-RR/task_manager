import asyncio
import pytest
from sqlalchemy import insert

from app.config import settings
import json
from app.database import Model, async_sessionmaker, engine, TaskOrm, UserOrm


@pytest.fixture(scope="session", autouse=True)
async def prepare_db():
    assert settings.MODE == "TEST"

    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
        await conn.run_sync(Model.metadata.create_all)

    def open_mock_json(model: str):
        with open(f"app/tests/mock_{model}.json", encoding="utf-8", mode="r") as file:
            return json.load(file)

    users = open_mock_json("users")
    tasks = open_mock_json("tasks")

    async with async_sessionmaker() as session:
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
