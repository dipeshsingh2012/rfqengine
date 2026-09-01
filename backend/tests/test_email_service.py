import pytest
from app.services.email_service import EmailService

@pytest.mark.asyncio
async def test_send_email_success():
    service = EmailService()
    result = await service.send_email("test@example.com", "Hello", "World")
    assert result is True

@pytest.mark.asyncio
async def test_send_email_invalid_recipient():
    service = EmailService()
    result = await service.send_email("invalid-email", "Hello", "World")
    assert result is False

@pytest.mark.asyncio
async def test_send_bulk_emails():
    service = EmailService()
    recipients = ["a@test.com", "b@test.com", "invalid"]
    summary = await service.send_bulk_emails(recipients, "Bulk", "Body")
    
    assert summary["total"] == 3
    assert summary["success"] == 2
    assert summary["failed"] == 1
