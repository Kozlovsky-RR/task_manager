from pydantic import BaseModel, EmailStr, ConfigDict


class SUserAdd(BaseModel):
    name: str
    email: EmailStr
    password: str


class SUser(SUserAdd):
    id: int


class SUserID(BaseModel):
    ok: bool = True
    user_id: int


class SUserSchema(BaseModel):
    model_config = ConfigDict(strict=True)

    id: int
    name: str
    password: bytes
    email: EmailStr | None = None
    active: bool = True
