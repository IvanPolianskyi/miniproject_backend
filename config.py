from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    SECRET_KEY: str
    DATABASE_URL: str = os.environ.get("DATABASE_URL")
    if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+asyncpg://", 1)
    EXPIRES_IN: int
    FACE_API_KEY: str
    FACE_API_URL: str

    class Config:
        env_file = ".env"

settings = Settings()
