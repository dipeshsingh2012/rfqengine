import pytest
from unittest.mock import AsyncMock, MagicMock
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import DatabaseManager

@pytest.mark.asyncio
async def test_database_connection_lifecycle():
    """
    Verifies that the get_session generator correctly manages the 
    session lifecycle using the async context manager.
    """
    # Setup: Mock the session and the factory
    mock_session = AsyncMock(spec=AsyncSession)
    
    # The session_factory is a callable that returns an async context manager
    # We need to mock the __aenter__ and __aexit__ of the object returned by the factory
    mock_context_manager = MagicMock()
    mock_context_manager.__aenter__ = AsyncMock(return_value=mock_session)
    mock_context_manager.__aexit__ = AsyncMock(return_value=None)
    
    mock_factory = MagicMock(return_value=mock_context_manager)

    # Initialize manager with a dummy URL
    db_manager = DatabaseManager("postgresql+asyncpg://user:pass@localhost/testdb")
    # Inject the mock factory
    db_manager.session_factory = mock_factory

    # Execution: Iterate through the generator
    async for session in db_manager.get_session():
        assert session == mock_session
        # Verify the session was actually yielded
        assert session.close is not None

    # Verification: Ensure the context manager was entered and exited
    mock_context_manager.__aenter__.assert_called_once()
    mock_context_manager.__aexit__.assert_called_once()

@pytest.mark.asyncio
async def test_session_yields_correct_type():
    """
    Verifies that the yielded object is compatible with AsyncSession.
    """
    # Setup: Use a real AsyncSession mock to ensure type compatibility
    mock_session = AsyncMock(spec=AsyncSession)
    
    mock_context_manager = MagicMock()
    mock_context_manager.__aenter__ = AsyncMock(return_value=mock_session)
    mock_context_manager.__aexit__ = AsyncMock(return_value=None)
    
    mock_factory = MagicMock(return_value=mock_context_manager)

    db_manager = DatabaseManager("postgresql+asyncpg://user:pass@localhost/testdb")
    db_manager.session_factory = mock_factory

    # Execution
    async for session in db_manager.get_session():
        # In a mocked environment, we verify it matches our spec
        assert session == mock_session
        # Check that it behaves like an AsyncSession (has required async methods)
        assert hasattr(session, "execute")
        assert hasattr(session, "commit")
        assert hasattr(session, "rollback")
