from fastapi import APIRouter, Depends, Form, HTTPException, status
from pydantic import BaseModel
from app.auth import utils as auth_utils
from app.repository.user_repository import UserRepository
from app.schemas.user_schemas import SUserSchema
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/jwt/login/")


class TokenInfo(BaseModel):
    access_token: str
    token_type: str


router = APIRouter(prefix="/jwt", tags=["JWT"])


async def validate_auth_user(username: str = Form(), password: str = Form()):
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid username or password"
    )

    user_db = await UserRepository.get_user_by_username(username)

    if user_db is None:
        raise unauthed_exc

    if (
        auth_utils.validate_password(
            password=password, hashed_password=user_db.password
        )
        is False
    ):
        raise unauthed_exc

    # if user_db.active is False:
    #     raise HTTPException(
    #         status_code=status.HTTP_403_FORBIDDEN, detail="user inactive"
    #     )
    return user_db


# def get_current_token_payload(token: str = Depends(oauth2_scheme)) -> SUserSchema:
#     try:
#         payload = auth_utils.decode_jwt(token=token)
#     except InvalidTokenError as e:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED, detail=f"invalid token error: {e}"
#         )
#     return payload


# async def get_current_auth_user(
#     payload: dict = Depends(get_current_token_payload),
# ) -> SUserSchema:
#     username: str | None = payload.get("username")
#     user_db = await UserRepository.get_user_by_username(username)
#
#     if user := user_db.get(username):
#         return user
#     raise HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="token invalid (user not found)",
#     )


# def get_current_active_auth_user(user: SUserSchema = Depends(get_current_auth_user)):
#     if user.active:
#         return user
#     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="user inactive")


@router.post("/login/", response_model=TokenInfo)
def auth_user_issue_jwt(user: SUserSchema = Depends(validate_auth_user)):
    jwt_payload = {"sub": user.id, "username": user.name, "email": user.email}
    token = auth_utils.encode_jwt(jwt_payload)
    return TokenInfo(access_token=token, token_type="Bearer")


# @router.get("/users/me/")
# def auth_user_check_self_info(
#     user: SUserSchema = Depends(get_current_active_auth_user),
# ):
#     return {"username": user.name, "email": user.email}
