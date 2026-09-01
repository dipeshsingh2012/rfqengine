import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI
from app.api.v1.endpoints.health import router

# Create a dummy app for testing the router
app = FastAPI()
app.include_router(router)

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "project" in data
