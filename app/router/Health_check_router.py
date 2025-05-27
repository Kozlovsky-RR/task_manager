"""Файл с ручкой для проверки состояния приложения."""

from fastapi import APIRouter


router = APIRouter(prefix="/health", tags=["Healthcheck"])


@router.get("")
async def health_check():
    """Функция для проверки состояния приложения."""
    return {"status": "ok"}
