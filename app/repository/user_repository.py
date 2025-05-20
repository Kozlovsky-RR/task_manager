from app.schemas.user_schemas import SUser
from app.models.users_models import UserOrm
from app.repository.base_repository import BaseRepository


class UserRepository(BaseRepository):
    """Класс для подключения к таблице users"""

    model = UserOrm
    schemas = SUser
