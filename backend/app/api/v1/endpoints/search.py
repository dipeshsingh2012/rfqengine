from fastapi import APIRouter, Query, HTTPException, status
from typing import List, Dict, Any
from pydantic import BaseModel, Field

router = APIRouter()

class SearchResponse(BaseModel):
    results: List[Dict[str, Any]]
    count: int

@router.get("/", response_model=SearchResponse)
async def search_documents(
    query: str = Query(..., min_length=1),
    top_k: int = Query(10, ge=1, le=100)
):
    """
    Search for documents based on a natural language query.
    """
    # Mock implementation for demonstration
    if not query:
        raise HTTPException(status_code=422, detail="Query cannot be empty")
        
    return {
        "results": [{"id": "doc_1", "text": f"Result for {query}"}],
        "count": 1
    }
