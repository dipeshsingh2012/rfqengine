from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    """
    Application settings managed via environment variables.
    """
    # Core App Settings
    SERVICE_NAME: str = "RFQ Engine"
    DEBUG: bool = False
    
    # GCP Settings
    # Added to prevent Pydantic ValidationError: extra_forbidden
    gcp_project_id: str = ""
    gcp_region: str = "us-central1"
    
    # Search/Vector DB Settings
    VECTOR_DB_URL: str = "http://localhost:6333"
    
    model_config = SettingsConfigDict(
        env_file=".env", 
        extra="ignore"  # Changed to ignore to be more resilient to env variations
    )

settings = Settings()
