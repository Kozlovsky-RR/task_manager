from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).parent.parent
DB_PATH = BASE_DIR / "task_management.db"


class DbSettings(BaseModel):
    url: str = f"sqlite+aiosqlite:///{DB_PATH}"
    echo: bool = False


class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "certs" / "jwt-private.txt"
    public_key_path: Path = BASE_DIR / "certs" / "jwt-public.txt"
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 15


class Settings(BaseSettings):
    auth_jwt: AuthJWT = AuthJWT()
    db: DbSettings = DbSettings()


settings = Settings()
