import pytest
import asyncio
from app.services.export_service import ExportService
from app.services.tenant_service import TenantDataService

@pytest.mark.asyncio
async def test_csv_formula_injection_protection():
    service = ExportService()
    data = [{"id": "1", "note": "=SUM(A1:A10)"}, {"id": "2", "note": "+100"}]
    headers = ["id", "note"]
    
    chunks = []
    async for chunk in service.generate_csv_stream(data, headers):
        chunks.append(chunk)
    
    full_content = "".join(chunks)
    assert "'=SUM(A1:A10)" in full_content
    assert "'+100" in full_content

@pytest.mark.asyncio
async def test_filename_sanitization():
    service = ExportService()
    unsafe_name = "../../etc/passwd\r\n"
    safe_name = service.sanitize_filename(unsafe_name)
    assert safe_name == "etcpasswd"
    assert "../" not in safe_name

@pytest.mark.asyncio
async def test_tenant_isolation_logic():
    service = TenantDataService()
    
    alpha_data = await service.get_tenant_records("tenant_alpha")
    assert len(alpha_data) == 2
    assert alpha_data[0]["name"] == "Project Alpha"
    
    empty_data = await service.get_tenant_records("unknown_tenant")
    assert len(empty_data) == 0

@pytest.mark.asyncio
async def test_streaming_generator_integrity():
    service = ExportService()
    data = [{"a": "1", "b": "2"}, {"a": "3", "b": "4"}]
    headers = ["a", "b"]
    
    chunks = []
    async for chunk in service.generate_csv_stream(data, headers):
        chunks.append(chunk)
    
    assert len(chunks) == 3
    assert "a,b" in chunks[0]
    assert "1,2" in chunks[1]
    assert "3,4" in chunks[2]
