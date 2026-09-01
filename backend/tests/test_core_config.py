import pytest
from app.core.config import settings

def test_settings_defaults():
    """Verify that default settings are loaded correctly."""
    assert settings.PROJECT_NAME == "Autonomous Agentic Fleet"
    assert settings.API_V1_STR == "/api/v1"

def test_settings_types():
    """Verify type integrity of settings."""
    assert isinstance(settings.DEBUG, bool)
    assert isinstance(settings.SMTP_PORT, int)
