from typing import List, Optional
from fastapi import APIRouter, Header, HTTPException, Query, status
from fastapi.responses import StreamingResponse

from app.models.webhook_audit import WebhookAuditLog
from app.services.webhook_audit_service import (
    webhook_audit_service,
    sanitize_filename_part,
)

router = APIRouter(prefix="/webhook-audit", tags=["Webhook Audit Stream"])

@router.post("/", response_model=WebhookAuditLog, status_code=status.HTTP_201_CREATED)
async def record_webhook_audit(
    log: WebhookAuditLog,
    x_tenant_id: str = Header(..., alias="X-Tenant-ID")
):
    """Record a webhook execution audit event securely isolated by tenant."""
    if log.tenant_id != x_tenant_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Tenant ID mismatch between payload and header."
        )
    return await webhook_audit_service.log_event(log)

@router.get("/export", response_class=StreamingResponse)
async def export_webhook_audit_stream(
    event_type: Optional[str] = Query(None),
    x_tenant_id: str = Header(..., alias="X-Tenant-ID")
):
    """Stream webhook audit logs as a memory-efficient sanitized CSV file."""
    sanitized_tenant = sanitize_filename_part(x_tenant_id)
    if not sanitized_tenant:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid tenant identifier for export."
        )

    logs = await webhook_audit_service.get_audit_logs(tenant_id=x_tenant_id, event_type=event_type)
    
    filename = f"webhook_audit_{sanitized_tenant}.csv"
    
    return StreamingResponse(
        webhook_audit_service.generate_audit_csv_chunks(logs),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )
