import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_search_valid_query_positive():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/search?q=hello&top_k=3")
        assert response.status_code == 200
        assert response.json()["query"] == "hello"
        assert response.json()["top_k"] == 3

@pytest.mark.asyncio
async def test_search_empty_question_negative():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/search?q=")
        assert response.status_code == 400

@pytest.mark.asyncio
async def test_search_out_of_bounds_top_k_negative():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/search?q=test&top_k=-1")
        assert response.status_code == 400
