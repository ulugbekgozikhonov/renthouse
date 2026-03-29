from typing import Literal

from pydantic import PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    python_env: Literal["development", "production"]
    bot_token: str
    postgres_url: PostgresDsn
    redis_url: RedisDsn

    model_config = SettingsConfigDict(extra="ignore")


settings = Settings()  # type: ignore
