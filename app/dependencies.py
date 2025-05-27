"""Файл с зависимостью для получения юзера из токена."""

from datetime import UTC, datetime

from fastapi import Depends, Request
from jwt import PyJWTError

from app.auth.utils import decode_jwt
from app.exceptions import (
    IncorrectTokenFormatException,
    TokenAbsentException,
    TokenExpiredException,
    UserIsNotPresentException,
)
from app.logger import logger
from app.repository.user_repository import UserRepository


def get_token(request: Request):
    """Получение токена."""
    token = request.headers.get("Authorization")
    if not token:
        raise TokenAbsentException
    return token.split()[1]


async def get_user(token: str = Depends(get_token)):
    """Получение юзера."""
    try:
        payload = decode_jwt(token=token)
    except PyJWTError:
        raise IncorrectTokenFormatException
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.now(UTC).timestamp()):
        raise TokenExpiredException
    user_id: str = payload.get("sub")
    if not user_id:
        logger.exception("The user does not exist")
        raise UserIsNotPresentException
    user = await UserRepository.find_by_id(id=int(user_id))
    if not user:
        logger.exception("The user does not exist")
        raise UserIsNotPresentException
    return user
