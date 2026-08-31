from fastapi import FastAPI
from app.core.config import settings

def create_application() -> FastAPI:
    """
    Factory function to create the FastAPI application instance.
    """
    app = FastAPI(
        title=settings.app_name,
        openapi_url=f"{settings.api_v1_prefix}/openapi.json",
        docs_url="/docs",
        redoc_url="/redoc"
    )
    
    # Add middleware, routers, and exception handlers here
    
    return app

app = create_application()
