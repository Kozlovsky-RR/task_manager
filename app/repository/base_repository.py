"""Базовый класс для работы с таблицами."""

from app.database import new_session

from sqlalchemy import select, insert, delete, update


class BaseRepository:
    """Базовый класс для подключения к таблице."""

    model = None
    schema = None

    @classmethod
    async def find_by_id(cls, **filter_by) -> schema:
        """Метод для поиска по id."""
        async with new_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls, **filter_by) -> schema:
        """Метод для поиска какого либо объекта."""
        async with new_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls, **filter_by) -> list[schema]:
        """Метод для поиска всех объектов."""
        async with new_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            models = result.scalars().all()
            schemas = [cls.schema.model_validate(model) for model in models]
            return schemas

    @classmethod
    async def add(cls, **data) -> None:
        """Метод для добавления какого либо объекта."""
        async with new_session() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete(cls, **filter_by) -> None:
        """Метод для удаления какого либо объекта."""
        async with new_session() as session:
            query = delete(cls.model).filter_by(**filter_by)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def update(cls, model_id: int, **new_values) -> None:
        """Метод для изменения какого либо объекта."""
        async with new_session() as session:
            query = update(cls.model).filter_by(id=model_id).values(**new_values)
            await session.execute(query)
            await session.commit()
