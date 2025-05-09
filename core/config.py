from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).parent.parent


class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "certs" / "jwt-private.txt"
    public_key_path: Path = BASE_DIR / "certs" / "jwt-public.txt"
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 15


class Settings(BaseSettings):
    auth_jwt: AuthJWT = AuthJWT()


settings = Settings()
