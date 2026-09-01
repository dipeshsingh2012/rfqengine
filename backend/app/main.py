from fastapi import FastAPI
from app.api.v1.endpoints import health, search

app = FastAPI(
    title="RFQ Engine API",
    version="1.0.0"
)

# Include Routers
app.include_router(health.router, tags=["health"])
# The prefix must match the test expectations (/api/v1/search)
app.include_router(search.router, prefix="/api/v1/search", tags=["search"])

@app.get("/")
async def root():
    return {"message": "Welcome to the RFQ Engine API"}
