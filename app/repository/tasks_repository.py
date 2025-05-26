"""Файл для подключения к таблице tasks."""

from app.schemas.tasks_schemas import SchemaTask
from app.models.tasks_models import TaskOrm
from app.repository.base_repository import BaseRepository


class TaskRepository(BaseRepository):
    """Класс для подключения к таблице tasks."""

    model = TaskOrm
    schema = SchemaTask
