from pathlib import Path
from typing import Literal

from pydantic import model_validator
from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    MODE: Literal["DEV", "TEST", "PROD"]
    DB_NAME: str
    TEST_DB_NAME: str
    private_key_path: Path = BASE_DIR / "certs" / "jwt-private.txt"
    public_key_path: Path = BASE_DIR / "certs" / "jwt-public.txt"
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 15

    class Config:
        env_file = ".env"


settings = Settings()
