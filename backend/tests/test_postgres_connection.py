import pytest
import pytest_asyncio
from sqlalchemy import text
from app.core.database import engine

@pytest.mark.asyncio
async def test_database_connection():
    """Verifies that the engine can execute a simple query."""
    try:
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT 1"))
            assert result.scalar() == 1
    except Exception as e:
        pytest.fail(f"Database connection failed: {e}")
