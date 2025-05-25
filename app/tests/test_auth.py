"""Тесты регистрации и входа пользователя."""

from httpx import AsyncClient
import pytest


@pytest.mark.parametrize(
    "name, email, password, status_code",
    [
        ("Yan", "Y@gmail.com", "33333", 200),
        ("Ruslan", "agmail.com", "33333", 422),
        ("Alex", "al@gmail.com", "22222", 409),
        ("Ruslan", "a@gmail.com", "asdfasd", 200),
    ],
)
async def test_add_user(name, email, password, status_code, ac: AsyncClient):
    response = await ac.post(
        "/auth/register/", params={"name": name, "email": email, "password": password}
    )

    assert response.status_code == status_code


@pytest.mark.parametrize(
    "email, password, status_code",
    [
        ("rus@gmail.com", "12345", 200),
        ("rus@gmail.com", "asdf", 401),
        ("q@gmail.com", "asdf", 409),
    ],
)
async def test_auth_user_issue_jwt(email, password, status_code, ac: AsyncClient):
    response = await ac.post(
        "/auth/login/", data={"username": email, "password": password}
    )

    assert response.status_code == status_code
