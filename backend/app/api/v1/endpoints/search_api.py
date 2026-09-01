from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

router = APIRouter()

class SearchQuery(BaseModel):
    query: str = Field(..., min_length=1)
    top_k: int = Field(default=5, ge=1, le=100)

@router.post("/search")
async def search_documents(request: SearchQuery) -> Dict[str, Any]:
    """
    Performs semantic search across indexed documents.
    Includes boundary validation for top_k via Pydantic.
    """
    # In a real app, this calls a vector database service
    # For now, we simulate a successful response
    return {
        "query": request.query,
        "results": [
            {"id": "doc_1", "score": 0.98, "text": "Sample result text"},
            {"id": "doc_2", "score": 0.85, "text": "Another result"}
        ],
        "metadata": {"top_k_requested": request.top_k}
    }
