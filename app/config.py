"""Файл конфигураций проекта."""

from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    """Класс настроек проекта."""

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )
    MODE: Literal["DEV", "TEST", "PROD"]
    DB_NAME: str
    TEST_DB_NAME: str
    private_key_path: Path = BASE_DIR / "certs" / "jwt-private.txt"
    public_key_path: Path = BASE_DIR / "certs" / "jwt-public.txt"
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 15


settings = Settings()
