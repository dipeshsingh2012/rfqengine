import pytest
from unittest.mock import AsyncMock, MagicMock
from typing import Any, Dict, List, Optional

# Absolute imports ensure pytest collection succeeds when run from backend/
from app.services.user_service import UserService

@pytest.mark.asyncio
async def test_get_user_by_id_success():
    """Test successful user retrieval."""
    service = UserService()
    user_id = "123"
    user = await service.get_user_by_id(user_id)
    
    assert user is not None
    assert user["id"] == user_id
    assert user["name"] == "Test User"

@pytest.mark.asyncio
async def test_get_user_by_id_not_found():
    """Test retrieval when user does not exist."""
    service = UserService()
    user = await service.get_user_by_id("error")
    
    assert user is None

@pytest.mark.asyncio
async def test_list_users():
    """Test listing all users."""
    service = UserService()
    users = await service.list_users()
    
    assert isinstance(users, list)
    assert len(users) == 2
    assert users[0]["name"] == "Alice"

@pytest.mark.asyncio
async def test_user_service_mocking():
    """Demonstrate proper mocking of the UserService."""
    mock_service = MagicMock(spec=UserService)
    mock_service.get_user_by_id = AsyncMock(return_value={"id": "mock", "name": "Mock User"})
    
    result = await mock_service.get_user_by_id("mock")
    
    assert result["name"] == "Mock User"
    mock_service.get_user_by_id.assert_awaited_once_with("mock")
