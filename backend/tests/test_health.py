import pytest

def test_health_endpoint(client):
    """
    Verifies that the health check endpoint returns a 200 OK and correct structure.
    """
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "project" in data

def test_root_endpoint(client):
    """
    Verifies the root endpoint is accessible.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome to" in response.json()["message"]
