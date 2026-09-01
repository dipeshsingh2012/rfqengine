import asyncio
from typing import Any, Dict, List, Optional

class EmailService:
    """Service for handling asynchronous email dispatch."""
    
    async def send_email(
        self, 
        recipient: str, 
        subject: str, 
        body: str, 
        attachments: Optional[List[str]] = None
    ) -> bool:
        """Sends an email. Returns True if successful."""
        # In a real implementation, this would interface with SMTP or an API
        if not recipient or "@" not in recipient:
            return False
        
        await asyncio.sleep(0.1)  # Simulate network latency
        return True

    async def send_bulk_emails(self, recipients: List[str], subject: str, body: str) -> Dict[str, int]:
        """Sends emails to multiple recipients and returns a summary."""
        success_count = 0
        for r in recipients:
            if await self.send_email(r, subject, body):
                success_count += 1
        
        return {
            "total": len(recipients),
            "success": success_count,
            "failed": len(recipients) - success_count
        }
