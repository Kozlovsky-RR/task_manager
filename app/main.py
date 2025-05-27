"""Файл подключения ручек к приложению."""

from fastapi import FastAPI

from app.auth.jwt_auth import router as auth_router
from app.router.Health_check_router import router as health_router
from app.router.tasks_router import router as tasks_router
from app.router.user_router import router as user_router

app = FastAPI(
    title="Менеджер задач", description="Менеджер работы с задачами.", version="1"
)

app.include_router(health_router)
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(tasks_router)
