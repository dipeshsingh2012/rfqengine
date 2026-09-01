import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture(scope="module")
def client():
    """
    Provides a TestClient instance for the FastAPI application.
    Scoped to 'module' to improve test performance.
    """
    with TestClient(app) as c:
        yield c

@pytest.fixture
def app_instance():
    """
    Returns the FastAPI app instance.
    """
    return app
