import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture(scope="module")
def client():
    """
    Provides a TestClient instance for the FastAPI application.
    Scoped to module to reuse the client across tests in a single file.
    """
    with TestClient(app) as c:
        yield c
