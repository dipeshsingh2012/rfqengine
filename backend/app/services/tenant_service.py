from typing import Any, Dict, List

class TenantDataService:
    """
    Service responsible for retrieving data scoped strictly to a specific tenant.
    In a production environment, this would interface with a database using 
    Row-Level Security (RLS) or tenant-specific schemas.
    """

    async def get_tenant_records(self, tenant_id: str) -> List[Dict[str, Any]]:
        mock_db = {
            "tenant_alpha": [
                {"id": "101", "name": "Project Alpha", "budget": "5000", "notes": "Standard"},
                {"id": "102", "name": "Project Beta", "budget": "12000", "notes": "=SUM(A1:A10)"},
            ],
            "tenant_beta": [
                {"id": "201", "name": "Beta Core", "budget": "99999", "notes": "High Priority"},
            ]
        }
        return mock_db.get(tenant_id, [])
