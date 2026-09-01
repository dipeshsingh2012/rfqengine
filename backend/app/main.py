from fastapi import FastAPI
from app.core.config import settings

def create_application() -> FastAPI:
    application = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
    )
    return application

app = create_application()
