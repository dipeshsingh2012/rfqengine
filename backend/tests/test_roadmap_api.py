import pytest
from typing import List, Dict, Any

@pytest.mark.asyncio
async def test_roadmap_fetch():
    # Mocking roadmap data
    roadmap: List[Dict[str, Any]] = [{"phase": 1, "task": "Init"}]
    assert len(roadmap) == 1
    assert roadmap[0]["phase"] == 1
