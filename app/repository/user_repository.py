"""Файл для подключения к таблице users."""

from app.models.users_models import UserOrm
from app.repository.base_repository import BaseRepository
from app.schemas.user_schemas import SchemaUser


class UserRepository(BaseRepository):
    """Класс для подключения к таблице users."""

    model = UserOrm
    schema = SchemaUser
