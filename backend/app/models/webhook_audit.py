from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field

class WebhookAuditLog(BaseModel):
    id: str
    tenant_id: str
    event_type: str
    payload: Dict[str, Any]
    status_code: int
    response_time_ms: float
    created_at: datetime = Field(default_factory=datetime.utcnow)
    error_message: Optional[str] = None
