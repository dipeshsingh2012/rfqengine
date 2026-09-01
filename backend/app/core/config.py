from __future__ import annotations

import json
import re
from functools import lru_cache
from typing import Any, Dict, List, Optional, Union
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings managed via environment variables.
    Defaults are provided for local development and testing.
    """
    PROJECT_NAME: str = "Autonomous Agentic Fleet"
    app_name: str = "Autonomous Agentic Fleet"
    app_version: str = "0.2.0"
    API_V1_STR: str = "/api/v1"
    api_v1_prefix: str = "/api/v1"
    env: str = "local"  # "local", "dev", "staging", "prod"
    DEBUG: bool = True
    debug: bool = True
    SECRET_KEY: str = "test-secret-key-for-development-and-testing-only"
    TENANT_ID_HEADER: str = "X-Tenant-ID"
    gcp_project_id: Optional[str] = "test-project-id"

    @property
    def is_production(self) -> bool:
        return self.env.lower() in ("prod", "production")

    @property
    def is_local(self) -> bool:
        return self.env.lower() in ("local", "dev", "test")

    # Database Settings
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/rfpengine"
    postgres_user: Optional[str] = None
    postgres_password: Optional[str] = None
    postgres_host: Optional[str] = None
    postgres_port: int = 5432
    postgres_db: Optional[str] = None
    postgres_ssl: bool = True

    @property
    def DATABASE_URL(self) -> str:
        """Alias for backward compatibility with tests expecting uppercase attribute."""
        return self.effective_database_url

    @property
    def effective_database_url(self) -> str:
        """
        Returns the resolved database URL from either database_url or individual POSTGRES_* components.
        Ensures asyncpg driver prefix.
        """
        url = self.database_url
        if self.postgres_host and self.postgres_user and self.postgres_password and self.postgres_db:
            ssl_param = "?ssl=require" if self.postgres_ssl else ""
            url = (
                f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}"
                f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}{ssl_param}"
            )
        
        if url.startswith("postgresql://") and "+asyncpg" not in url:
            url = url.replace("postgresql://", "postgresql+asyncpg://", 1)
        return url

    model_config = SettingsConfigDict(
        env_file=(".env.local", ".env", "../.env.local", "../.env", "../../.env"),
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
