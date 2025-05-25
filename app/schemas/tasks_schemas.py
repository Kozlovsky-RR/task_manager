"""Схемы задач."""

from pydantic import BaseModel, ConfigDict
from app.database import Status


class STaskAdd(BaseModel):
    """Схема для добавления задачи."""

    model_config = ConfigDict(from_attributes=True)

    name_tsk: str
    description: str
    status: Status


class STask(STaskAdd):
    """Схема модели таблицы tasks."""

    id: int
    user_id: int
