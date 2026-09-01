from fastapi import FastAPI
from app.api.v1.endpoints import health, search

app = FastAPI(
    title="RFQ Engine API",
    description="Autonomous Agentic Fleet RFQ Management System",
    version="1.0.0"
)

# Include Routers
app.include_router(health.router, prefix="/api/v1", tags=["system"])
app.include_router(search.router, prefix="/api/v1", tags=["search"])

@app.get("/")
async def root():
    return {"message": "Welcome to RFQ Engine API"}
