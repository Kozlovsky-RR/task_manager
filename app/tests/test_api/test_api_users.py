"""Тесты работы с пользователями."""

from httpx import AsyncClient
import pytest


async def test_get_users(authenticated_ac: AsyncClient):
    response = await authenticated_ac.get(url="/users")
    assert response.status_code == 200


@pytest.mark.parametrize(
    "user_id, status_code",
    [
        (1, 200),
        (4, 409),
        (0.1, 422),
        (-1, 409),
        ("asdfa", 422),
    ],
)
async def test_get_user(user_id, status_code, authenticated_ac: AsyncClient):
    response = await authenticated_ac.get(url=f"/users/{user_id}")
    assert response.status_code == status_code


@pytest.mark.parametrize(
    "user_id, name, email, password, status_code",
    [
        (3, "Yan", "Y@gmail.com", "12345", 200),
        (4, "Yan", "Y@gmail.com", "12345", 409),
        (3, "Yan", "asdf", "12345", 422),
    ],
)
async def test_update_user(
    user_id, name, email, password, status_code, authenticated_ac: AsyncClient
):
    response = await authenticated_ac.put(
        url=f"/users/{user_id}",
        params={"name": name, "email": email, "password": password},
    )

    assert response.status_code == status_code


@pytest.mark.parametrize(
    "user_id, status_code",
    [
        (1, 200),
        (4, 409),
        (0.1, 422),
        (-1, 409),
        ("asdfa", 422),
    ],
)
async def test_delete_user(user_id, status_code, authenticated_ac: AsyncClient):
    response = await authenticated_ac.get(url=f"/users/{user_id}")

    assert response.status_code == status_code
