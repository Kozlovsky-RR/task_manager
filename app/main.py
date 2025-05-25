"""Файл подключения ручек к приложению."""

from fastapi import FastAPI

from app.router.tasks_router import router as tasks_router
from app.router.user_router import router as user_router
from app.auth.jwt_auth import router as auth_router


app = FastAPI()


app.include_router(auth_router)
app.include_router(user_router)
app.include_router(tasks_router)
