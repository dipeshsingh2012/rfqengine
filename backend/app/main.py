from fastapi import FastAPI
from app.core.config import settings
from app.api.v1 import health

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Include routers with the correct prefix from settings
app.include_router(health.router, prefix=f"{settings.API_V1_STR}/health", tags=["health"])

@app.get("/")
async def root():
    return {"message": "Welcome to the RFQ Engine API"}
