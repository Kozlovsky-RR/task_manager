"""Схемы задач."""

from pydantic import BaseModel, ConfigDict, Field

from app.database import Status


class STaskAdd(BaseModel):
    """Схема для добавления задачи."""

    model_config = ConfigDict(from_attributes=True)

    name: str = Field(max_length=30)
    description: str
    status: Status


class STask(STaskAdd):
    """Схема модели таблицы tasks."""

    id: int
    user_id: int
