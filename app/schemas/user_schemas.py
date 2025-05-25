"""Схемы пользователей."""

from pydantic import BaseModel, EmailStr, ConfigDict


class SUserAdd(BaseModel):
    """Схема для добавления пользователя."""

    model_config = ConfigDict(from_attributes=True)

    name: str
    email: EmailStr
    password: str


class SUser(SUserAdd):
    """Схема модели таблицы users."""

    id: int
