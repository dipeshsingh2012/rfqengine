import pytest
import httpx
from unittest.mock import AsyncMock, Mock
from app.services.slack_service import SlackService

@pytest.mark.asyncio
async def test_send_notification_success():
    """Test successful notification delivery."""
    # Setup
    mock_client = AsyncMock(spec=httpx.AsyncClient)
    webhook_url = "https://hooks.slack.com/services/test"
    service = SlackService(client=mock_client, webhook_url=webhook_url)

    # Mock a successful response
    mock_response = Mock(spec=httpx.Response)
    mock_response.status_code = 200
    # raise_for_status does nothing on success
    mock_response.raise_for_status = Mock() 
    
    mock_client.post.return_value = mock_response

    # Execute
    success = await service.send_notification("Hello World")

    # Assert
    assert success is True
    mock_client.post.assert_called_once_with(webhook_url, json={"text": "Hello World"}, timeout=10.0)

@pytest.mark.asyncio
async def test_send_notification_http_error():
    """Test handling of HTTP error statuses (e.g., 500)."""
    # Setup
    mock_client = AsyncMock(spec=httpx.AsyncClient)
    webhook_url = "https://hooks.slack.com/services/test"
    service = SlackService(client=mock_client, webhook_url=webhook_url)

    # Create a mock response that will trigger an error
    mock_response = Mock(spec=httpx.Response)
    mock_response.status_code = 500
    
    # We must mock raise_for_status as a regular Mock (not AsyncMock) 
    # because it is a synchronous method in the httpx library.
    # We set the side_effect to raise the actual httpx exception.
    error_request = Mock(spec=httpx.Request)
    mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
        "Internal Server Error", 
        request=error_request, 
        response=mock_response
    )

    mock_client.post.return_value = mock_response

    # Execute
    success = await service.send_notification("Test message")

    # Assert
    assert success is False
    mock_client.post.assert_called_once()

@pytest.mark.asyncio
async def test_send_notification_network_error():
    """Test handling of network-level connection errors."""
    # Setup
    mock_client = AsyncMock(spec=httpx.AsyncClient)
    webhook_url = "https://hooks.slack.com/services/test"
    service = SlackService(client=mock_client, webhook_url=webhook_url)

    # Simulate a connection timeout/error
    mock_client.post.side_effect = httpx.ConnectError("Connection failed")

    # Execute
    success = await service.send_notification("Test message")

    # Assert
    assert success is False
