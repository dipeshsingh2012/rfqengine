import pytest
from typing import Any, Dict

def test_health_endpoint(client) -> None:
    """
    Verifies that the health check endpoint returns a 200 status and correct structure.
    """
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    
    data: Dict[str, Any] = response.json()
    assert data["status"] == "ok"
    assert "project" in data

def test_root_endpoint(client) -> None:
    """
    Verifies the root endpoint is reachable.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to RFQ Engine API"}
