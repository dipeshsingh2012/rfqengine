from fastapi import APIRouter, Query, HTTPException
from pydantic import BaseModel, Field
from typing import List

router = APIRouter()

class SearchQuery(BaseModel):
    query: str = Field(..., min_length=1)
    top_k: int = Field(default=5, ge=1, le=100)

@router.post("/")
async def search(payload: SearchQuery):
    return {
        "results": [{"id": i, "score": 0.99} for i in range(payload.top_k)],
        "count": payload.top_k
    }
