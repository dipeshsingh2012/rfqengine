from typing import Any, Optional
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Application settings managed via environment variables.
    """
    PROJECT_NAME: str = "Autonomous Agentic Fleet"
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = False
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/rfpengine"
    REDIS_URL: Optional[str] = None
    
    # GCP Configuration - Added to fix AttributeError in services
    GCP_PROJECT_ID: str = "default-gcp-project"
    GCP_REGION: str = "us-central1"
    
    # Tenant/Security
    SECRET_KEY: str = "super-secret-key-change-in-production"
    
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def gcp_project_id(self) -> str:
        """Compatibility property for code accessing lowercase attribute."""
        return self.GCP_PROJECT_ID

settings = Settings()
