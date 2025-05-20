from pydantic_settings import BaseSettings
from pydantic import SecretStr
from functools import lru_cache
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    # Database settings
    DB_URL: SecretStr = os.environ.get("DB_URL")


@lru_cache
def get_settings() -> Settings:
    return Settings()
