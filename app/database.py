from sqlalchemy import ForeignKey, NullPool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import enum

from app.config import settings


if settings.MODE == "TEST":
    DB_URL = f"sqlite+aiosqlite:///{settings.TEST_DB_NAME}"
    DB_PARAMS = {"poolclass": NullPool}
else:
    DB_URL = f"sqlite+aiosqlite:///{settings.DB_NAME}"
    DB_PARAMS = {}

engine = create_async_engine(url=DB_URL, echo=False, **DB_PARAMS)
new_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


class Status(str, enum.Enum):
    new = "новая"
    in_process = "в процессе"
    completed = "завершена"


class UserOrm(Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    tasks: Mapped[list["TaskOrm"]] = relationship(back_populates="user")


class TaskOrm(Model):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name_tsk: Mapped[str]
    description: Mapped[str]
    status: Mapped[Status]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    user: Mapped["UserOrm"] = relationship(back_populates="tasks")
