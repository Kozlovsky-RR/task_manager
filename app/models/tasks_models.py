"""Модель sqlalchemy для создания таблицы tasks."""

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Model, Status

if TYPE_CHECKING:
    from app.models.users_models import UserOrm


class TaskOrm(Model):
    """Модель таблицы для создания задач."""

    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(length=30))
    description: Mapped[str]
    status: Mapped[Status]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    user: Mapped["UserOrm"] = relationship(back_populates="tasks")

    def __str__(self):
        return f"Нужно {self.name_tsk}"
