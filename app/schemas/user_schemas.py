"""Схемы пользователей."""

from pydantic import BaseModel, EmailStr, ConfigDict


class SchemaUserAdd(BaseModel):
    """Схема для добавления пользователя."""

    model_config = ConfigDict(from_attributes=True)

    name: str
    email: EmailStr
    password: str


class SchemaUser(SchemaUserAdd):
    """Схема модели таблицы users."""

    id: int
