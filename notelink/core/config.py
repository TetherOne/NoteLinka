from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="envs/.main-env",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="FAST_API_HH__",
        arbitrary_types_allowed=True,
    )
    db: DatabaseConfig


settings = Settings()
