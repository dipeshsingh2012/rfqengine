import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_search_valid_query_positive():
    """
    Tests valid search query.
    Fixed: AsyncClient instantiation using ASGITransport.
    """
    # In modern httpx, we pass the app via ASGITransport
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/search?q=test-query")
        assert response.status_code == 200
        assert "results" in response.json()

@pytest.mark.asyncio
async def test_search_empty_question_negative():
    """
    Tests search with empty query.
    Fixed: AsyncClient instantiation using ASGITransport.
    """
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/search?q=")
        # Assuming 400 Bad Request for empty query
        assert response.status_code == 400

@pytest.mark.asyncio
async def test_search_out_of_bounds_top_k_negative():
    """
    Tests search with invalid top_k parameter.
    Fixed: AsyncClient instantiation using ASGITransport.
    """
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/search?q=test&top_k=-1")
        assert response.status_code == 400
