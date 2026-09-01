from fastapi import APIRouter, Header, HTTPException, Depends
from fastapi.responses import StreamingResponse
from app.services.tenant_service import TenantDataService
from app.services.export_service import ExportService
from typing import Optional

router = APIRouter()

def get_tenant_service() -> TenantDataService:
    return TenantDataService()

def get_export_service() -> ExportService:
    return ExportService()

@router.get("/export/csv")
async def export_tenant_data(
    x_tenant_id: str = Header(..., alias="X-Tenant-ID"),
    tenant_service: TenantDataService = Depends(get_tenant_service),
    export_service: ExportService = Depends(get_export_service)
) -> StreamingResponse:
    """
    Securely exports tenant data as a CSV stream.
    Requires 'X-Tenant-ID' header for multi-tenant isolation.
    """
    data = await tenant_service.get_tenant_records(x_tenant_id)
    
    if not data:
        raise HTTPException(status_code=404, detail="No data found for this tenant")

    headers = list(data[0].keys())
    safe_filename = export_service.sanitize_filename(f"export_{x_tenant_id}.csv")

    return StreamingResponse(
        export_service.generate_csv_stream(data, headers),
        media_type="text/csv",
        headers={
            "Content-Disposition": f"attachment; filename=\"{safe_filename}\""
        }
    )
