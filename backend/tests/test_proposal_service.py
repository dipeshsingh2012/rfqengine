import pytest
import asyncio
from app.services.proposal_service import ProposalService

@pytest.mark.asyncio
async def test_approve_proposal_success():
    """Tests successful approval within the same tenant."""
    service = ProposalService()
    tenant_id = "tenant-abc"
    proposal_id = "prop-1"
    
    result = await service.approve_proposal(proposal_id, tenant_id)
    
    assert result["id"] == proposal_id
    assert result["status"] == "approved"
    assert result["tenant_id"] == tenant_id

@pytest.mark.asyncio
async def test_approve_proposal_unauthorized_tenant():
    """Tests that a tenant cannot approve a proposal belonging to another tenant."""
    service = ProposalService()
    attacker_tenant_id = "tenant-xyz"
    target_proposal_id = "prop-1"  # Belongs to tenant-abc
    
    with pytest.raises(PermissionError) as excinfo:
        await service.approve_proposal(target_proposal_id, attacker_tenant_id)
    
    assert "Access denied" in str(excinfo.value)

@pytest.mark.asyncio
async def test_approve_proposal_not_found():
    """Tests error handling for non-existent proposal IDs."""
    service = ProposalService()
    
    with pytest.raises(ValueError) as excinfo:
        await service.approve_proposal("non-existent", "tenant-abc")
    
    assert "not found" in str(excinfo.value)

@pytest.mark.asyncio
async def test_stream_proposals_isolation():
    """Tests that streaming only returns data for the requested tenant."""
    service = ProposalService()
    tenant_id = "tenant-abc"
    
    proposals = []
    async for proposal in service.stream_proposals(tenant_id):
        proposals.append(proposal)
    
    # tenant-abc has 2 proposals in our mock DB
    assert len(proposals) == 2
    for p in proposals:
        assert p["tenant_id"] == tenant_id

@pytest.mark.asyncio
async def test_stream_proposals_empty_for_new_tenant():
    """Tests that a tenant with no proposals receives an empty stream."""
    service = ProposalService()
    tenant_id = "tenant-new"
    
    proposals = []
    async for proposal in service.stream_proposals(tenant_id):
        proposals.append(proposal)
        
    assert len(proposals) == 0
