from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()

@router.get("/health")
async def health_check():
    """
    Returns the health status of the service.
    """
    return {
        "service": settings.SERVICE_NAME,
        "status": "ok"
    }
