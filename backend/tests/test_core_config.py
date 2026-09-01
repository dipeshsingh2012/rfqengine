from app.core.config import settings

def test_database_url_default():
    assert "postgresql" in settings.DATABASE_URL
