"""Файл с ручкой для проверки состояния приложения."""

from fastapi import APIRouter
from app.logger import logger

router = APIRouter(prefix="/health", tags=["Healthcheck"])


@router.get("")
async def health_check():
    """Функция для проверки состояния приложения."""
    logger.info("Healthcheck called")
    return {"status": "ok"}
