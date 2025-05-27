"""Файл для создания бд."""

import enum

from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

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
    """Базовая модель для таблиц."""

    pass


class Status(str, enum.Enum):
    """Состояние задачи."""

    new = "новая"
    in_process = "в процессе"
    completed = "завершена"
