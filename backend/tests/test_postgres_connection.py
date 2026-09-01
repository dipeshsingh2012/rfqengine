import pytest
import pytest_asyncio
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.postgres import DatabaseManager

# Using a local sqlite memory DB for testing to avoid requiring a live Postgres instance during collection
TEST_DB_URL = "sqlite+aiosqlite:///:memory:"

@pytest_asyncio.fixture
async def db_manager() -> DatabaseManager:
    """Fixture to provide a clean database manager for each test."""
    manager = DatabaseManager(TEST_DB_URL)
    yield manager
    await manager.close()

@pytest_asyncio.fixture
async def db_session(db_manager: DatabaseManager) -> AsyncGenerator[AsyncSession, None]:
    """Fixture to provide an async session."""
    async for session in db_manager.get_session():
        yield session

@pytest.mark.asyncio
async def test_database_connection_lifecycle(db_manager: DatabaseManager):
    """Verify the database manager can initialize and dispose of the engine."""
    assert db_manager.engine is not None
    await db_manager.close()

@pytest.mark.asyncio
async def test_session_yields_correct_type(db_session: AsyncGenerator[AsyncSession, None]):
    """Verify that the session generator yields an AsyncSession object."""
    # We need to iterate the generator to get the actual session
    async for session in db_session:
        assert isinstance(session, AsyncSession)
