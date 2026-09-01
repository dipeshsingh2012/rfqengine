from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def get_health():
    """System health check endpoint."""
    return {"status": "ok", "version": "1.0.0"}
