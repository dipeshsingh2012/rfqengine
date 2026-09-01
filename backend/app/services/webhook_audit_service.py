import csv
import io
import re
from typing import Any, Dict, Iterator, List, Optional
from app.models.webhook_audit import WebhookAuditLog

def sanitize_csv_cell(value: Any) -> str:
    """Strip whitespace and escape formula injection characters."""
    val_str = str(value) if value is not None else ""
    cleaned = val_str.strip()
    dangerous_chars = ('=', '+', '-', '@', '\t', '\r')
    if cleaned.startswith(dangerous_chars):
        return f"'{val_str}"
    return val_str

def sanitize_filename_part(part: str) -> str:
    """Strictly sanitize filename part against path traversal and header splitting."""
    return re.sub(r"[^a-zA-Z0-9_-]", "", str(part).strip())

class WebhookAuditService:
    def __init__(self):
        # In-memory store for demonstration. In production, this would be a DB.
        self._storage: List[WebhookAuditLog] = []

    async def log_event(self, log: WebhookAuditLog) -> WebhookAuditLog:
        self._storage.append(log)
        return log

    async def get_audit_logs(
        self, tenant_id: str, event_type: Optional[str] = None
    ) -> List[WebhookAuditLog]:
        return [
            log for log in self._storage
            if log.tenant_id == tenant_id and (not event_type or log.event_type == event_type)
        ]

    async def get_log_by_id(self, log_id: str, tenant_id: str) -> Optional[WebhookAuditLog]:
        for log in self._storage:
            if log.id == log_id:
                if log.tenant_id != tenant_id:
                    return None  # Isolation breach attempt
                return log
        return None

    def generate_audit_csv_chunks(self, logs: List[WebhookAuditLog]) -> Iterator[str]:
        """Memory-efficient streaming generator that yields CSV rows incrementally."""
        output = io.StringIO()
        writer = csv.writer(output)
        
        headers = ["id", "tenant_id", "event_type", "status_code", "response_time_ms", "created_at", "error_message"]
        writer.writerow(headers)
        yield output.getvalue()
        output.seek(0)
        output.truncate(0)
        
        for log in logs:
            row_data = [
                sanitize_csv_cell(log.id),
                sanitize_csv_cell(log.tenant_id),
                sanitize_csv_cell(log.event_type),
                sanitize_csv_cell(log.status_code),
                sanitize_csv_cell(log.response_time_ms),
                sanitize_csv_cell(log.created_at.isoformat()),
                sanitize_csv_cell(log.error_message or "")
            ]
            writer.writerow(row_data)
            yield output.getvalue()
            output.seek(0)
            output.truncate(0)

webhook_audit_service = WebhookAuditService()
