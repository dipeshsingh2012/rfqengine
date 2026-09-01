import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    """Fixture to provide a TestClient for synchronous tests."""
    with TestClient(app) as c:
        yield c

def test_health_endpoint(client):
    """
    Tests the health endpoint.
    Fixed: Assertion mismatch (expected 'ok', not 'healthy').
    """
    response = client.get("/health")
    assert response.status_code == 200
    # The API returns {"status": "ok"}
    assert response.json() == {"status": "ok"}

def test_config_loading():
    """Tests that settings are loaded correctly."""
    from app.core.config import settings
    assert settings.PROJECT_NAME == "Autonomous Agentic Fleet"
    assert hasattr(settings, "gcp_project_id")
