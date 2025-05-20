"""Файл с зависимостью для получения юзера из токена"""

from datetime import datetime, UTC
from fastapi import Request, Depends
from jwt import PyJWTError
from app.auth.utils import decode_jwt
from app.exeptions import (
    TokenExpiredException,
    TokenAbsentException,
    IncorrectTokenFormatException,
    UserIsNotPresentException,
)
from app.repository.user_repository import UserRepository


def get_token(request: Request):
    token = request.headers.get("Authorization")
    if not token:
        raise TokenAbsentException
    return token.split()[1]


async def get_user(token: str = Depends(get_token)):
    try:
        payload = decode_jwt(token=token)
    except PyJWTError:
        raise IncorrectTokenFormatException
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.now(UTC).timestamp()):
        raise TokenExpiredException
    user_id: str = payload.get("sub")
    if not user_id:
        raise UserIsNotPresentException
    user = await UserRepository.find_by_id(id=int(user_id))
    if not user:
        raise UserIsNotPresentException
    return user
