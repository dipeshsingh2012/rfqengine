from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_search_valid_query_positive():
    response = client.post("/api/v1/search/", json={"query": "test", "top_k": 5})
    assert response.status_code == 200
    assert len(response.json()["results"]) == 5

def test_search_empty_question_negative():
    response = client.post("/api/v1/search/", json={"query": "", "top_k": 5})
    assert response.status_code == 422

def test_search_out_of_bounds_top_k_negative():
    response = client.post("/api/v1/search/", json={"query": "test", "top_k": 0})
    assert response.status_code == 422
