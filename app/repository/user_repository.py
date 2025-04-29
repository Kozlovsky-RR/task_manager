from app.database import new_session, UserOrm
from sqlalchemy import select
from app.schemas.user_schemas import SUser, SUserAdd
from app.auth.utils import hash_password


class UserRepository:
    @classmethod
    async def add_user(cls, user: SUserAdd):
        async with new_session() as session:
            user_dict = user.model_dump()
            user_dict["password"] = hash_password(user_dict["password"])
            user = UserOrm(**user_dict)
            session.add(user)
            await session.flush()
            await session.commit()
            return user.id

    @classmethod
    async def get_all_users(cls) -> list[SUser]:
        async with new_session() as session:
            query = select(UserOrm)
            result = await session.execute(query)
            users_models = result.scalars().all()
            # добавить преобразование к списку
            return users_models

    @classmethod
    async def get_user(cls, user_id: int) -> SUser | bool:
        async with new_session() as session:
            user = await session.get(UserOrm, user_id)
            if user:
                return user
            return False

    @classmethod
    async def update_user(cls, user_id: int, new_user: SUserAdd):
        async with new_session() as session:
            user = await session.get(UserOrm, user_id)
            if not user:
                return False
            user.name = new_user.name
            user.email = new_user.email
            user.password = hash_password(new_user.password)
            await session.commit()
            return user_id

    @classmethod
    async def delete_user(cls, user_id):
        async with new_session() as session:
            user = await session.get(UserOrm, user_id)
            if user:
                await session.delete(user)
                await session.commit()
                return user_id
            else:
                return False

    @classmethod
    async def get_user_by_username(cls, username):
        async with new_session() as session:
            result = await session.execute(
                select(UserOrm).where(UserOrm.name == username)
            )
            return result.scalar_one_or_none()
