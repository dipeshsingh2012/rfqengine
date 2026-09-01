import logging
import httpx
from typing import Any, Dict

logger = logging.getLogger(__name__)

class SlackService:
    """Service to handle sending notifications to Slack via Webhooks."""

    def __init__(self, client: httpx.AsyncClient, webhook_url: str):
        self.client = client
        self.webhook_url = webhook_url

    async def send_notification(self, message: str) -> bool:
        """
        Sends a text message to the configured Slack webhook.
        
        Returns:
            bool: True if successful, False if an error occurred.
        """
        if not self.webhook_url:
            logger.error("Slack webhook URL is not configured.")
            return False

        try:
            payload: Dict[str, Any] = {"text": message}
            response = await self.client.post(
                self.webhook_url, 
                json=payload,
                timeout=10.0
            )
            
            # raise_for_status is a SYNCHRONOUS method in httpx
            response.raise_for_status()
            return True

        except httpx.HTTPStatusError as exc:
            logger.error(f"Slack API returned error status: {exc.response.status_code} - {exc}")
            return False
        except httpx.RequestError as exc:
            logger.error(f"Network error occurred while contacting Slack: {exc}")
            return False
        except Exception as exc:
            logger.error(f"Unexpected error in SlackService: {exc}")
            return False
