"""Тесты работы с задачами."""

from httpx import AsyncClient
import pytest


@pytest.mark.parametrize(
    "name_tsk, status, description, status_code",
    [
        ("прочитать", "новая", "2 книги", 200),
        ("прочитать", "asdf", "2 книги", 422),
    ],
)
async def test_add_task(
    name_tsk, status, description, status_code, authenticated_ac: AsyncClient
):
    response = await authenticated_ac.post(
        url="/tasks",
        params={"name_tsk": name_tsk, "status": status, "description": description},
    )

    assert response.status_code == status_code


async def test_get_tasks(authenticated_ac: AsyncClient):
    response = await authenticated_ac.get(url="/tasks")

    assert response.status_code == 200


@pytest.mark.parametrize(
    "task_id, status_code",
    [
        (1, 200),
        (4, 403),
        (0.1, 422),
        (-1, 403),
        ("asdfa", 422),
    ],
)
async def test_get_task(task_id, status_code, authenticated_ac: AsyncClient):
    response = await authenticated_ac.get(url=f"/tasks/{task_id}")

    assert response.status_code == status_code


@pytest.mark.parametrize(
    "task_id, name_tsk, status, description, status_code",
    [
        (2, "прочитать", "новая", "2 книги", 200),
        (4, "прочитать", "новая", "2 книги", 403),
        (3, "прочитать", "asdf", "2 книги", 422),
    ],
)
async def test_update_task(
    task_id, name_tsk, status, description, status_code, authenticated_ac: AsyncClient
):
    response = await authenticated_ac.put(
        url=f"/tasks/{task_id}",
        params={"name_tsk": name_tsk, "status": status, "description": description},
    )

    assert response.status_code == status_code


@pytest.mark.parametrize(
    "task_id, status_code",
    [
        (1, 200),
        (4, 403),
        (0.1, 422),
        (-1, 403),
        ("asdfa", 422),
    ],
)
async def test_delete_task(task_id, status_code, authenticated_ac: AsyncClient):
    response = await authenticated_ac.delete(url=f"/tasks/{task_id}")

    assert response.status_code == status_code
