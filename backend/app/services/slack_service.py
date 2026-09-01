import logging
import httpx
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

class SlackService:
    """Service to handle outgoing Slack notifications via Webhooks."""

    def __init__(self, webhook_url: str, timeout: float = 5.0):
        if not webhook_url.startswith("https://hooks.slack.com/"):
            raise ValueError("Invalid Slack webhook URL")
        self.webhook_url = webhook_url
        self.timeout = timeout

    async def send_notification(self, message: str, payload: Optional[Dict[str, Any]] = None) -> bool:
        """
        Sends a message to the configured Slack webhook.
        
        Args:
            message: The text content of the notification.
            payload: Optional additional JSON payload for Slack blocks/attachments.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        data = {"text": message}
        if payload:
            data.update(payload)

        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(self.webhook_url, json=data)
                response.raise_for_status()
                return True
        except httpx.HTTPStatusError as e:
            logger.error(f"Slack API returned error status: {e.response.status_code} - {e.response.text}")
        except httpx.RequestError as e:
            logger.error(f"Slack network error occurred: {str(e)}")
        except Exception as e:
            logger.error(f"Unexpected error sending Slack notification: {str(e)}")
        
        return False
