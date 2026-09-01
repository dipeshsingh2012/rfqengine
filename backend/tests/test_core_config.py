import pytest
from app.core.config import Settings, get_settings_async

@pytest.mark.asyncio
async def test_get_settings_async():
    """
    Test the async generator for settings to ensure 
    compatibility with async dependency injection.
    """
    async for settings in get_settings_async():
        assert isinstance(settings, Settings)
        assert settings.PROJECT_NAME == "Autonomous Agentic Fleet"

def test_settings_defaults():
    """
    Test that default settings are correctly applied when 
    no environment variables are present.
    """
    settings = Settings()
    assert settings.PROJECT_NAME == "Autonomous Agentic Fleet"
    assert settings.API_V1_STR == "/api/v1"
    assert settings.DEBUG is False

def test_settings_env_override(monkeypatch):
    """
    Test that environment variables correctly override 
    the default settings values.
    """
    # Mocking environment variables
    monkeypatch.setenv("PROJECT_NAME", "Test Project")
    monkeypatch.setenv("DEBUG", "True")
    monkeypatch.setenv("DATABASE_URL", "postgresql://user:pass@localhost/db")

    settings = Settings()
    
    assert settings.PROJECT_NAME == "Test Project"
    assert settings.DEBUG is True
    assert settings.DATABASE_URL == "postgresql://user:pass@localhost/db"

def test_settings_invalid_type_raises_error(monkeypatch):
    """
    Test that providing an invalid type for a boolean field 
    raises a validation error.
    """
    monkeypatch.setenv("DEBUG", "not-a-boolean")
    
    with pytest.raises(Exception):
        Settings()
