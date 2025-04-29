from sqlalchemy import select
from app.database import new_session, TaskOrm
from app.schemas.tasks_schemas import STaskAdd, STask


class TaskRepository:
    @classmethod
    async def add_task(cls, task: STaskAdd):
        async with new_session() as session:
            task_dict = task.model_dump()
            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def get_all_tasks(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            """Спросить у Артема про эту строку"""
            # task_schemas = [STask.model_validate(task_model) for task_model in task_models]
            return task_models

    @classmethod
    async def get_task(cls, task_id: int) -> STask | bool:
        async with new_session() as session:
            task = await session.get(TaskOrm, task_id)
            if task:
                return task
            return False

    @classmethod
    async def update_task(cls, task_id: int, new_task: STaskAdd):
        async with new_session() as session:
            task = await session.get(TaskOrm, task_id)
            if not task:
                return False
            task.name_tsk = new_task.name_tsk
            task.description = new_task.description
            task.status = new_task.status
            await session.commit()
            return task_id

    @classmethod
    async def delete_task(cls, task_id):
        async with new_session() as session:
            task = await session.get(TaskOrm, task_id)
            if task:
                await session.delete(task)
                await session.commit()
                return task_id
            else:
                return False
