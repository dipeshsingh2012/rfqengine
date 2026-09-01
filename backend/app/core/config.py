from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "RFQ Engine API"
    app_version: str = "1.0.0"
    debug: bool = False
    
    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
