import asyncio
import logging
from typing import Any, Dict, List, AsyncGenerator, Optional

logger = logging.getLogger(__name__)

class ProposalService:
    """
    Service handling proposal lifecycles, including approval workflows
    and memory-efficient data streaming.
    """

    def __init__(self):
        # In a real scenario, this would involve a Database Session or Repository
        self._mock_db: List[Dict[str, Any]] = [
            {"id": "prop-1", "tenant_id": "tenant-abc", "status": "pending", "title": "New UI Design"},
            {"id": "prop-2", "tenant_id": "tenant-abc", "status": "pending", "title": "API Refactor"},
            {"id": "prop-3", "tenant_id": "tenant-xyz", "status": "pending", "title": "Database Migration"},
        ]

    async def approve_proposal(self, proposal_id: str, tenant_id: str) -> Dict[str, Any]:
        """
        Approves a proposal after validating tenant ownership.
        """
        # Simulate DB latency
        await asyncio.sleep(0.01)

        for proposal in self._mock_db:
            if proposal["id"] == proposal_id:
                # Security: Multi-tenant isolation check
                if proposal["tenant_id"] != tenant_id:
                    logger.warning(f"Unauthorized access attempt by {tenant_id} on {proposal_id}")
                    raise PermissionError("Access denied: Tenant mismatch.")
                
                proposal["status"] = "approved"
                logger.info(f"Proposal {proposal_id} approved for tenant {tenant_id}")
                return proposal

        raise ValueError(f"Proposal {proposal_id} not found.")

    async def stream_proposals(self, tenant_id: str) -> AsyncGenerator[Dict[str, Any], None]:
        """
        Memory-efficient generator that yields proposals for a specific tenant.
        Prevents OOM by yielding one record at a time.
        """
        for proposal in self._mock_db:
            # Security: Multi-tenant isolation
            if proposal["tenant_id"] == tenant_id:
                # Simulate processing time
                await asyncio.sleep(0.01)
                yield proposal
