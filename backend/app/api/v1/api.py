from fastapi import APIRouter
from app.api.v1.endpoints import (
    document_parser,
    email_service,
    search_api,
    health
)

api_router = APIRouter()

# Register all feature-specific routers
api_router.include_router(document_parser.router, prefix="/documents", tags=["Documents"])
api_router.include_router(email_service.router, prefix="/email", tags=["Email"])
api_router.include_router(search_api.router, prefix="/search", tags=["Search"])
api_router.include_router(health.router, prefix="/health", tags=["System"])
