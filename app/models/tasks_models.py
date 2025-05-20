"""Модель sqlalchemy для создания таблицы tasks"""

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Model, Status
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.models.users_models import UserOrm


class TaskOrm(Model):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name_tsk: Mapped[str]
    description: Mapped[str]
    status: Mapped[Status]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    user: Mapped["UserOrm"] = relationship(back_populates="tasks")

    def __str__(self):
        return f"Нужно {self.name_tsk}"
