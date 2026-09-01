import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_search_valid_query_positive():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/v1/search/?query=test_query&top_k=5")
    
    assert response.status_code == 200
    assert "results" in response.json()

@pytest.mark.asyncio
async def test_search_empty_question_negative():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # FastAPI returns 422 for validation errors (min_length=1)
        response = await ac.get("/api/v1/search/?query=&top_k=5")
    
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_search_out_of_bounds_top_k_negative():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # top_k < 1 should trigger 422
        response = await ac.get("/api/v1/search/?query=test&top_k=0")
    
    assert response.status_code == 422
