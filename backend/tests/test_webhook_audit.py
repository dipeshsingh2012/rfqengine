import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services.webhook_audit_service import webhook_audit_service

client = TestClient(app)

@pytest.fixture(autouse=True)
def clear_storage():
    webhook_audit_service._storage.clear()

def test_record_and_export_webhook_audit():
    headers = {"X-Tenant-ID": "tenant-123"}
    payload = {
        "id": "wh_1",
        "tenant_id": "tenant-123",
        "event_type": "payment.succeeded",
        "payload": {"amount": 100},
        "status_code": 200,
        "response_time_ms": 50.5,
        "error_message": "=SUM(1,2)"
    }
    
    # Test Recording
    response = client.post("/api/v1/webhook-audit/", json=payload, headers=headers)
    assert response.status_code == 201
    
    # Test Export
    export_res = client.get("/api/v1/webhook-audit/export/csv", headers=headers)
    assert export_res.status_code == 200
    assert "'=SUM(1,2)" in export_res.text  # Sanitized

def test_tenant_isolation_access():
    # Setup: Record log for Tenant A
    client.post(
        "/api/v1/webhook-audit/", 
        json={"id": "log_a", "tenant_id": "A", "event_type": "t", "payload": {}, "status_code": 200, "response_time_ms": 1},
        headers={"X-Tenant-ID": "A"}
    )

    # Attempt access by Tenant B
    res = client.get("/api/v1/webhook-audit/log_a", headers={"X-Tenant-ID": "B"})
    assert res.status_code == 404  # Isolated

def test_record_mismatch_forbidden():
    payload = {"id": "wh_2", "tenant_id": "tenant-A", "event_type": "t", "payload": {}, "status_code": 200, "response_time_ms": 1}
    res = client.post("/api/v1/webhook-audit/", json=payload, headers={"X-Tenant-ID": "tenant-B"})
    assert res.status_code == 403
