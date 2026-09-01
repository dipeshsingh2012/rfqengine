from fastapi import FastAPI
from app.api.v1.api import api_router

def create_app() -> FastAPI:
    """
    Factory function to create the FastAPI application.
    Ensures all routers are correctly mounted under the /api/v1 prefix.
    """
    app = FastAPI(
        title="Autonomous Agentic Fleet API",
        version="1.0.0",
        docs_url="/docs",
        openapi_url="/openapi.json"
    )

    # Include the central API router which aggregates all feature routers
    app.include_router(api_router, prefix="/api/v1")

    @app.get("/health", tags=["System"])
    async def health_check():
        return {"status": "healthy"}

    return app

app = create_app()
