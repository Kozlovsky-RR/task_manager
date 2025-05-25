"""Модель sqlalchemy для создания таблицы users."""

from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from app.database import Model


if TYPE_CHECKING:
    from app.models.tasks_models import TaskOrm


class UserOrm(Model):
    """Таблица для создания пользователей."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    tasks: Mapped[list["TaskOrm"]] = relationship(back_populates="user")

    def __str__(self):
        return f"Пользователь {self.email}"
