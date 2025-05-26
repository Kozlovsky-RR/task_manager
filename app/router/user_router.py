"""Файл с ручками для пользователей."""

from typing import Annotated
from fastapi import APIRouter, Depends

from app.auth.utils import hash_password
from app.exceptions import UserIsNotPresentException
from app.repository.user_repository import UserRepository
from app.schemas.user_schemas import SUser, SUserAdd
from app.auth.jwt_auth import oauth2_scheme


router = APIRouter(
    prefix="/users", tags=["Пользователи"], dependencies=[Depends(oauth2_scheme)]
)


@router.get("")
async def get_users() -> list:
    """Ручка для получения всех пользователей."""
    user = await UserRepository.find_all()
    return user


@router.get("/{user_id}")
async def get_one_user(user_id: int) -> SUser | None:
    """Ручка для получения пользователя по id."""
    user = await UserRepository.find_by_id(id=user_id)
    if not user:
        raise UserIsNotPresentException
    return user


@router.put("/{user_id}")
async def update_user(
    user_id: int,
    new_user: Annotated[SUserAdd, Depends()],
) -> None:
    """Ручка для изменения данных пользователя."""
    check_user = await UserRepository.find_by_id(id=user_id)
    if not check_user:
        raise UserIsNotPresentException
    hashed_password = hash_password(new_user.password)
    await UserRepository.update(
        user_id, name=new_user.name, email=new_user.email, password=hashed_password
    )


@router.delete("/{user_id}")
async def delete_user(user_id: int) -> None:
    """Ручка для удаления пользователя."""
    check_user = await UserRepository.find_by_id(id=user_id)
    if not check_user:
        raise UserIsNotPresentException
    await UserRepository.delete(id=user_id)
