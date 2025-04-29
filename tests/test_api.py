import pytest
from httpx import AsyncClient, ASGITransport
from main import app
from app.schemas.user_schemas import SUserAdd
import json

# @pytest.mark.asyncio
# async def test_get_users():
#     async with AsyncClient(
#         transport=ASGITransport(app=app), base_url="http://test"
#     ) as ac:
#         response = await ac.get("/users")
#         assert response.status_code == 401
#         data = response.json()
#         assert data == {"detail": "Not authenticated"}


@pytest.mark.asyncio
async def test_post_users():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.post(
            "/users",
            json={"name": "rus", "email": "rus@rut.com", "password": "1234"},
        )
        print(response)
        assert response.status_code == 200
