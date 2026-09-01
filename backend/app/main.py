from fastapi import FastAPI
from app.api.v1.endpoints import search, health
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME)

# Include routers
app.include_router(search.router, tags=["search"])
app.include_router(health.router, tags=["health"])

@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.APP_NAME}"}
