from app.core.config import Settings

def test_database_url_default():
    settings = Settings()
    # The driver is postgresql+asyncpg, not just postgresql
    assert 'postgresql+asyncpg://' in settings.DATABASE_URL
