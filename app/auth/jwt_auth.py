"""Файл для регистрации и входа пользователя."""

from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from app.auth import utils as auth_utils
from app.auth.token_schemas import TokenInfo
from app.auth.utils import hash_password, validate_auth_user
from app.exceptions import CheckUserException
from app.logger import logger
from app.repository.user_repository import UserRepository
from app.schemas.user_schemas import SchemaUser, SchemaUserAdd

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login/")
router = APIRouter(prefix="/auth", tags=["reg/log"])


@router.post("/register/")
async def add_user(user: Annotated[SchemaUserAdd, Depends()]):
    """Роутер для регистрации пользователя."""
    check_user = await UserRepository.find_one_or_none(email=user.email)
    if check_user:
        logger.exception("The user already exists")
        raise CheckUserException
    hashed_password = hash_password(user.password)
    await UserRepository.add(name=user.name, email=user.email, password=hashed_password)
    logger.info("The user is registered")


@router.post("/login/", response_model=TokenInfo)
def auth_user_issue_jwt(user: SchemaUser = Depends(validate_auth_user)) -> TokenInfo:
    """Роутер для входа пользователя и создания jwt токена."""
    jwt_payload = {"sub": str(user.id), "username": user.name, "email": user.email}
    token = auth_utils.encode_jwt(jwt_payload)
    return TokenInfo(access_token=token, token_type="Bearer")
