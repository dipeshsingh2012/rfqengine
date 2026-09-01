from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    APP_NAME: str = Field(default="Autonomous Agentic Fleet")
    DEBUG: bool = False
    
    # Pydantic V2 way to define config
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
