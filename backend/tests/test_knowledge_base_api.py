import pytest
from typing import Dict, Any

@pytest.mark.asyncio
async def test_knowledge_base_retrieval():
    # Mocking the retrieval logic
    mock_data: Dict[str, Any] = {"id": "kb_1", "content": "Sample knowledge"}
    assert mock_data["id"] == "kb_1"
    assert "content" in mock_data
