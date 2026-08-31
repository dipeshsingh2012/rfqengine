from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Application settings managed via environment variables.
    Defaults are provided for local development.
    """
    app_name: str = "RFQ Engine"
    api_v1_prefix: str = "/api/v1"
    debug: bool = False
    
    # Pydantic V2 configuration
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

settings = Settings()
