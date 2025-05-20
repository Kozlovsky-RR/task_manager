"""Файл с функциями для регистрации и входа"""

from datetime import timedelta, datetime, UTC
from typing import Annotated

import jwt
import bcrypt
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.config import settings
from app.exeptions import UserIsNotPresentException, UnauthedException
from app.repository.user_repository import UserRepository
from app.schemas.user_schemas import SUser


def encode_jwt(
    payload: dict,
    private_key: str = settings.private_key_path.read_text(),
    algorithm: str = settings.algorithm,
    expire_minutes: int = settings.access_token_expire_minutes,
    expire_time_delta: timedelta | None = None,
) -> str:
    """Кодирование jwt токена"""
    to_encode = payload.copy()
    now = datetime.now(UTC)
    if expire_time_delta:
        expire = now + expire_time_delta
    else:
        expire = now + timedelta(minutes=expire_minutes)
    to_encode.update(exp=expire, iat=now)
    encoded = jwt.encode(to_encode, private_key, algorithm=algorithm)
    return encoded


def decode_jwt(
    token: str | bytes,
    public_key: str = settings.public_key_path.read_text(),
    algorithm: str = settings.algorithm,
) -> dict:
    """Декодирование jwt токена"""
    decoded = jwt.decode(
        token,
        public_key,
        algorithms=algorithm,
    )
    return decoded


def hash_password(password: str) -> bytes:
    """Хеширование пароля"""
    salt = bcrypt.gensalt()
    pwd_bytes: bytes = password.encode()
    return bcrypt.hashpw(pwd_bytes, salt)


def validate_password(password: str, hashed_password: bytes) -> bool:
    """Проверка пароля"""
    return bcrypt.checkpw(password=password.encode(), hashed_password=hashed_password)


async def validate_auth_user(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> SUser:
    """Проверка наличия пользователя"""
    user = await UserRepository.find_one_or_none(email=form_data.username)
    if user is None:
        raise UserIsNotPresentException
    if (
        validate_password(password=form_data.password, hashed_password=user.password)
        is False
    ):
        raise UnauthedException
    return user
