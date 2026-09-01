import pytest
from app.core.config import settings

def test_settings_project_name():
    """Verify that the project name is correctly loaded from settings."""
    assert settings.PROJECT_NAME == "Agentic Fleet"

def test_settings_api_version():
    """Verify the API version string."""
    assert settings.API_V1_STR == "/api/v1"
