import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture(scope="module")
def client():
    """
    Provides a TestClient instance for the FastAPI application.
    """
    with TestClient(app) as c:
        yield c
