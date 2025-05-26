"""Файл с ручками для задач."""

from typing import Annotated
from fastapi import APIRouter, Depends

from app.exceptions import NoAccessException
from app.repository.tasks_repository import TaskRepository
from app.schemas.tasks_schemas import STaskAdd, STask
from app.auth.jwt_auth import oauth2_scheme
from app.dependencies import get_user
from app.schemas.user_schemas import SUser

router = APIRouter(
    prefix="/tasks", tags=["Задачи"], dependencies=[Depends(oauth2_scheme)]
)


@router.post("")
async def add_task(
    task: Annotated[STaskAdd, Depends()], user: SUser = Depends(get_user)
) -> None:
    """Ручка для добавления задачи."""
    await TaskRepository.add(
        name=task.name,
        status=task.status,
        description=task.description,
        user_id=user.id,
    )


@router.get("")
async def get_tasks(user: SUser = Depends(get_user)) -> list[STask]:
    """Ручка для получения всех задач."""
    tasks = await TaskRepository.find_all(user_id=user.id)
    return tasks


@router.get("/{task_id}")
async def get_one_task(
    task_id: int,
    user: SUser = Depends(get_user),
) -> STask | None:
    """Ручка для получения задачи по id."""
    task = await TaskRepository.find_by_id(id=task_id, user_id=user.id)
    if task:
        return task
    raise NoAccessException


@router.put("/{task_id}")
async def update_task(
    task_id: int,
    new_task: Annotated[STaskAdd, Depends()],
    user: SUser = Depends(get_user),
) -> None:
    """Ручка для изменения информации о задаче."""
    old_task = await TaskRepository.find_by_id(id=task_id, user_id=user.id)
    if old_task:
        await TaskRepository.update(
            task_id,
            name=new_task.name,
            status=new_task.status,
            description=new_task.description,
        )
        return None
    else:
        raise NoAccessException


@router.delete("/{task_id}")
async def delete_task(
    task_id: int,
    user: SUser = Depends(get_user),
) -> None:
    """Ручка для удаления задачи."""
    task = await TaskRepository.find_by_id(id=task_id, user_id=user.id)
    if not task:
        """если обращаешься не к своей задаче или ее нет"""
        raise NoAccessException
    await TaskRepository.delete(id=task_id, user_id=user.id)
