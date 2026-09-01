import pytest
import httpx
from unittest.mock import AsyncMock, patch
from app.services.slack_service import SlackService

@pytest.mark.asyncio
async def test_send_notification_success():
    """Test successful Slack notification."""
    webhook_url = "https://hooks.slack.com/services/test/url"
    service = SlackService(webhook_url)

    # Mock httpx.AsyncClient.post
    with patch("httpx.AsyncClient.post", new_callable=AsyncMock) as mock_post:
        mock_post.return_value = httpx.Response(200, content=b"ok")
        
        result = await service.send_notification("Hello World")
        
        assert result is True
        mock_post.assert_called_once()
        # Verify the payload sent
        args, kwargs = mock_post.call_args
        assert kwargs["json"]["text"] == "Hello World"

@pytest.mark.asyncio
async def test_send_notification_http_error():
    """Test Slack notification handling of HTTP errors (e.g., 404, 500)."""
    webhook_url = "https://hooks.slack.com/services/test/url"
    service = SlackService(webhook_url)

    with patch("httpx.AsyncClient.post", new_callable=AsyncMock) as mock_post:
        # Simulate a 500 Internal Server Error
        mock_post.return_value = httpx.Response(500, content=b"Internal Server Error")
        # Ensure raise_for_status is called
        mock_post.return_value.raise_for_status.side_effect = httpx.HTTPStatusError(
            "Error", request=AsyncMock(), response=mock_post.return_value
        )
        
        result = await service.send_notification("Fail me")
        
        assert result is False

@pytest.mark.asyncio
async def test_send_notification_network_error():
    """Test Slack notification handling of network connectivity issues."""
    webhook_url = "https://hooks.slack.com/services/test/url"
    service = SlackService(webhook_url)

    with patch("httpx.AsyncClient.post", new_callable=AsyncMock) as mock_post:
        # Simulate a connection timeout/error
        mock_post.side_effect = httpx.RequestError("Connection failed")
        
        result = await service.send_notification("Network fail")
        
        assert result is False
