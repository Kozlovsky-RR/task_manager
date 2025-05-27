"""Тесты работы с таблицей users."""

import pytest

from app.auth.utils import hash_password
from app.models.users_models import UserOrm
from app.repository.user_repository import UserRepository


@pytest.mark.parametrize(
    "user_id, email, exists",
    [
        (1, "rus@gmail.com", True),
        (2, "al@gmail.com", True),
        (4, "asdf", False),
    ],
)
async def test_user_find_by_id(user_id, email, exists):
    user: UserOrm | None = await UserRepository.find_by_id(id=user_id)

    if exists:
        assert user
        assert user.id == user_id
        assert user.email == email
    else:
        assert not user


@pytest.mark.parametrize(
    "user_id, email, exists",
    [
        (1, "rus@gmail.com", True),
        (2, "al@gmail.com", True),
        (5, "asdf", False),
    ],
)
async def test_user_find_one_or_none(user_id, email, exists):
    user: UserOrm | None = await UserRepository.find_by_id(email=email)

    if exists:
        assert user
        assert user.id == user_id
        assert user.email == email
    else:
        assert not user


async def test_user_find_all():
    user = await UserRepository.find_all()
    assert len(user) == 3


async def test_user_add():
    hashed_password = hash_password("12345")
    await UserRepository.add(name="Leha", email="L@gmail.com", password=hashed_password)
    users = await UserRepository.find_all()
    assert len(users) > 3


async def test_user_delete():
    await UserRepository.delete(id=3)
    users = await UserRepository.find_all()
    assert len(users) == 2


async def test_user_update():
    hashed_password = hash_password("12345")
    await UserRepository.update(
        2, name="Leha", email="L@gmail.com", password=hashed_password
    )
    users = await UserRepository.find_by_id(id=2)
    assert users.email == "L@gmail.com"
