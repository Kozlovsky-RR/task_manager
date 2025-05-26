"""Тесты работы с таблицей tasks."""

from app.models.tasks_models import TaskOrm
from app.repository.tasks_repository import TaskRepository
import pytest


@pytest.mark.parametrize(
    "task_id, user_id, name, exists",
    [
        (1, 1, "Читать", True),
        (4, 2, "Бегать", True),
        (1, 2, "asdf", False),
    ],
)
async def test_task_find_by_id(task_id, user_id, name, exists):
    task: TaskOrm | None = await TaskRepository.find_by_id(id=task_id, user_id=user_id)

    if exists:
        assert task
        assert task.id == task_id
        assert task.user_id == user_id
        assert task.name == name
    else:
        assert not task


@pytest.mark.parametrize(
    "task_id, user_id, name, exists",
    [
        (1, 1, "Читать", True),
        (4, 2, "Бегать", True),
        (1, 2, "asdf", False),
    ],
)
async def test_task_find_by_id(task_id, user_id, name, exists):
    task: TaskOrm | None = await TaskRepository.find_by_id(id=task_id, user_id=user_id)

    if exists:
        assert task
        assert task.id == task_id
        assert task.user_id == user_id
        assert task.name == name
    else:
        assert not task


@pytest.mark.parametrize(
    "user_id, exists",
    [
        (1, True),
        (2, True),
        (4, False),
    ],
)
async def test_tasks_find_all(user_id, exists):
    tasks = await TaskRepository.find_all(user_id=user_id)
    if exists:
        assert tasks
        assert len(tasks) == 3
    else:
        assert not tasks


async def test_task_add():
    await TaskRepository.add(
        name="Делать зарядку", status="новая", description="Каждое утро", user_id=1
    )
    tasks = await TaskRepository.find_all(user_id=1)
    assert len(tasks) > 3


async def test_task_delete():
    await TaskRepository.delete(id=3)
    tasks = await TaskRepository.find_all(user_id=1)
    assert len(tasks) == 2


async def test_task_update():
    await TaskRepository.update(
        1,
        name="Делать зарядку",
        status="новая",
        description="Каждое утро",
        user_id=1,
    )
    task = await TaskRepository.find_by_id(id=1)
    assert task.name == "Делать зарядку"
