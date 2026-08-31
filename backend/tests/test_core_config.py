import pytest
from app.core.config import settings

def test_settings_load():
    assert settings.PROJECT_NAME == "Autonomous Agentic Fleet"
    assert isinstance(settings.DEBUG, bool)

def test_api_version_prefix():
    assert settings.API_V1_STR.startswith("/api/")
