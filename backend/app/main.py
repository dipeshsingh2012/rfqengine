from fastapi import FastAPI
from app.api.v1.endpoints import search, webhook, document, email, health

app = FastAPI(title="Audit API")

# Register routers
app.include_router(health.router, prefix="/api/v1")
app.include_router(search.router, prefix="/api/v1")
app.include_router(webhook.router, prefix="/api/v1")
app.include_router(document.router, prefix="/api/v1")
app.include_router(email.router, prefix="/api/v1")
