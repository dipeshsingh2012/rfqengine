from fastapi import APIRouter, Query, HTTPException, status
from typing import Optional

router = APIRouter()

@router.get("/search")
async def search(
    q: Optional[str] = Query(None),
    top_k: int = Query(default=5)
):
    """
    Search endpoint. 
    Returns 400 if query is empty or top_k is invalid.
    """
    if not q or q.strip() == "":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Query parameter 'q' cannot be empty"
        )
    
    if top_k <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="top_k must be a positive integer"
        )

    # Mock search logic
    return {
        "query": q,
        "top_k": top_k,
        "results": [{"id": 1, "score": 0.99, "text": f"Result for {q}"}]
    }
