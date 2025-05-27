from loguru import logger
import sys
import os
from pathlib import Path

# Папка для логов
log_path = Path("logs")
log_path.mkdir(exist_ok=True)


logger.add(
    sys.stdout, format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}", level="INFO"
)


logger.add(
    log_path / "app.log",
    rotation="10 MB",  # или "1 week", "00:00" (ежедневно)
    retention="1 day",  # сколько хранить
    compression="zip",  # архивировать старые
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    level="INFO",
)

__all__ = ["logger"]
