import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_record_and_export_webhook_audit():
    headers = {"X-Tenant-ID": "tenant-123"}
    payload = {
        "event_type": "payment.succeeded",
        "payload": {"amount": 100},
        "status": "success"
    }
    response = client.post("/api/v1/webhook-audit/", json=payload, headers=headers)
    assert response.status_code == 201
    data = response.json()
    assert data["event_type"] == "payment.succeeded"
    assert data["tenant_id"] == "tenant-123"

    # Export CSV test
    export_response = client.get("/api/v1/webhook-audit/export", headers=headers)
    assert export_response.status_code == 200
    assert "text/csv" in export_response.headers["content-type"]
    assert "payment.succeeded" in export_response.text

def test_tenant_isolation_forbidden():
    headers_1 = {"X-Tenant-ID": "tenant-A"}
    headers_2 = {"X-Tenant-ID": "tenant-B"}
    
    payload = {
        "event_type": "invoice.created",
        "payload": {"id": "inv_1"},
        "status": "success"
    }
    res = client.post("/api/v1/webhook-audit/", json=payload, headers=headers_1)
    assert res.status_code == 201
    audit_id = res.json()["id"]

    # Attempt access with tenant-B header should raise forbidden/404 isolation
    res_forbidden = client.get(f"/api/v1/webhook-audit/{audit_id}", headers=headers_2)
    assert res_forbidden.status_code in (403, 404)
