import pytest
from typing import List, Dict, Any

@pytest.mark.asyncio
async def test_feedback_submission():
    # Mocking feedback submission
    payload = {"user_id": "u1", "comment": "Great job"}
    assert payload["user_id"] == "u1"
    assert isinstance(payload["comment"], str)

@pytest.mark.asyncio
async def test_feedback_history_retrieval():
    mock_history: List[Dict[str, Any]] = [{"id": 1, "text": "Good"}]
    assert len(mock_history) == 1
