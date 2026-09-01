from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Application settings. 
    Uses Pydantic Settings to load from environment variables.
    """
    PROJECT_NAME: str = "RFQ Engine"
    API_V1_STR: str = "/api/v1"
    
    # Add other necessary settings here
    DATABASE_URL: str = "postgresql://user:pass@localhost:5432/db"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
