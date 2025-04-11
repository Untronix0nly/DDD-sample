from pathlib import Path

from pydantic import Field, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class ApplicationSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="", env_file=".env")
    project_name: str = Field(
        "API для управления библиотекой, сдачей книг",
        alias="PROJECT_NAME",
    )
    description: str = Field(
        "Пополнение книг, сдача и возврат книг",
        alias="DESCRIPTION",
    )
    version: str = Field("1.0.0", alias="VERSION")
    cache_host: str = Field("localhost", alias="CACHE_HOST")
    cache_port: int = Field(6379, alias="CACHE_PORT")
    base_dir: str = str(Path(__file__).parent.parent)
    debug: bool = Field(True, alias="DEBUG")
    postgres_conn: PostgresDsn = Field(
        "postgresql+asyncpg://app:123qwe@localhost:5342/users", alias="DATABASE_CONN"
    )
    echo: bool = Field(True, alias="ECHO")


settings = ApplicationSettings()
