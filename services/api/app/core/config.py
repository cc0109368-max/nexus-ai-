from functools import lru_cache

from pydantic import Field, SecretStr, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_env: str = "development"
    app_name: str = "NEXUS AI"
    api_v1_prefix: str = "/v1"
    secret_key: SecretStr = Field(default=SecretStr("unsafe-development-key-change-me"))
    access_token_expire_minutes: int = 20
    database_url: str = "postgresql+asyncpg://nexus:nexus_local_only@localhost:5432/nexus"
    redis_url: str = "redis://localhost:6379/0"
    gemini_api_key: SecretStr | None = None
    gemini_chat_model: str | None = None
    gemini_embedding_model: str | None = None
    cors_origins: str = "http://localhost:3000"
    max_upload_bytes: int = 20 * 1024 * 1024

    @model_validator(mode="after")
    def validate_production_secrets(self) -> "Settings":
        if self.is_production and len(self.secret_key.get_secret_value()) < 32:
            raise ValueError("SECRET_KEY must contain at least 32 characters in production")
        if (
            self.is_production
            and self.secret_key.get_secret_value() == "unsafe-development-key-change-me"
        ):
            raise ValueError("The development SECRET_KEY cannot be used in production")
        return self

    @property
    def cors_origin_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]

    @property
    def is_production(self) -> bool:
        return self.app_env.lower() == "production"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
