import pytest
from app.core.config import settings

def test_settings_project_name():
    """Verify that the project name is correctly loaded."""
    assert settings.PROJECT_NAME == "Autonomous Agentic Fleet"

def test_settings_tenant_header():
    """Verify the security header for multi-tenancy is correctly configured."""
    assert settings.TENANT_ID_HEADER == "X-Tenant-ID"

def test_settings_defaults():
    """Verify default values are present."""
    assert isinstance(settings.DEBUG, bool)
    assert "postgresql+asyncpg" in settings.DATABASE_URL
