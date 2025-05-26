"""Файл конфигураций проекта."""

from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Класс настроек проекта."""

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )
    MODE: Literal["DEV", "TEST", "PROD"]
    DB_NAME: str
    TEST_DB_NAME: str
    PRIVATE_KEY: str
    PUBLIC_KEY: str
    ALGORITHM: str
    access_token_expire_minutes: int = 15

    def get_private_key(self):
        return self.PRIVATE_KEY.replace("\\n", "\n")

    def get_public_key(self):
        return self.PUBLIC_KEY.replace("\\n", "\n")


settings = Settings()
