from typing import Annotated
from fastapi import APIRouter, Depends
from app.repository.user_repository import UserRepository
from app.schemas.user_schemas import SUser, SUserAdd, SUserID
from app.auth.jwt_auth import oauth2_scheme

router = APIRouter(prefix="/users", tags=["Пользователи"])


@router.post("")
async def add_user(user: Annotated[SUserAdd, Depends()]) -> SUserID:
    user_id = await UserRepository.add_user(user)
    return {"ok": True, "user_id": user_id}


@router.get("")
async def get_users(token: str = Depends(oauth2_scheme)) -> list[SUser]:
    user = await UserRepository.get_all_users()
    return user


@router.get("/{user_id}")
async def get_one_user(
    user_id: int, token: str = Depends(oauth2_scheme)
) -> SUser | None:
    user = await UserRepository.get_user(user_id)
    if not user:
        return None
    return user


@router.put("/{user_id}")
async def update_user(
    user_id: int,
    new_user: Annotated[SUserAdd, Depends()],
    token: str = Depends(oauth2_scheme),
) -> SUserID:
    completed = await UserRepository.update_user(user_id, new_user)
    if not completed:
        return {"ok": completed, "user_id": 0}
    return {"ok": True, "user_id": completed}


@router.delete("/{user_id}")
async def delete_user(user_id: int, token: str = Depends(oauth2_scheme)) -> SUserID:
    completed = await UserRepository.delete_user(user_id)
    if not completed:
        return {"ok": completed, "user_id": 0}
    return {"ok": True, "user_id": completed}
