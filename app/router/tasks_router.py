from typing import Annotated
from fastapi import APIRouter, Depends
from app.repository.tasks_repository import TaskRepository
from app.schemas.tasks_schemas import STaskAdd, STask, STaskID
from app.auth.jwt_auth import oauth2_scheme

router = APIRouter(prefix="/tasks", tags=["Задачи"])


@router.post("")
async def add_task(
    task: Annotated[STaskAdd, Depends()], token: str = Depends(oauth2_scheme)
) -> STaskID:
    task_id = await TaskRepository.add_task(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks(token: str = Depends(oauth2_scheme)) -> list[STask]:
    tasks = await TaskRepository.get_all_tasks()
    return tasks


@router.get("/{task_id}")
async def get_one_task(
    task_id: int, token: str = Depends(oauth2_scheme)
) -> STask | STaskID:
    task = await TaskRepository.get_task(task_id)
    if not task:
        return {"ok": task, "task_id": 0}
    return task


@router.put("/{task_id}")
async def update_task(
    task_id: int,
    new_task: Annotated[STaskAdd, Depends()],
    token: str = Depends(oauth2_scheme),
) -> STaskID:
    completed = await TaskRepository.update_task(task_id, new_task)
    if not completed:
        return {"ok": completed, "task_id": 0}
    return {"ok": True, "task_id": completed}


@router.delete("/{task_id}")
async def delete_task(task_id: int, token: str = Depends(oauth2_scheme)) -> STaskID:
    completed = await TaskRepository.delete_task(task_id)
    if not completed:
        return {"ok": completed, "task_id": 0}
    return {"ok": True, "task_id": completed}
