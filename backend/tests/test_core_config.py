import pytest
from app.core.config import Settings

def test_database_url_default():
    settings = Settings()
    assert "postgresql+asyncpg://" in settings.DATABASE_URL
