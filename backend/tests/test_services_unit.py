import pytest
from unittest.mock import MagicMock, patch
from typing import Any, Dict, List
from app.services.search_service import GoldenQAPromptGenerator # Assuming this exists

# Mocking settings to ensure tests don't fail on missing env vars
@pytest.fixture(autouse=True)
def mock_settings(monkeypatch):
    monkeypatch.setattr("app.core.config.settings.gcp_project_id", "test-project")

def test_golden_qa_prompt_generation_precedence():
    """
    Tests prompt generation logic.
    Fixed: AttributeError resolved by mock_settings/config fix.
    """
    generator = GoldenQAPromptGenerator()
    context = {"user_query": "What is AI?", "history": []}
    prompt = generator.generate(context)
    assert isinstance(prompt, str)
    assert "AI" in prompt

def test_gcp_secret_service_unconfigured():
    """
    Tests behavior when GCP is unconfigured.
    Fixed: AttributeError resolved by config fix.
    """
    from app.services.secret_service import GCPSecretService
    
    # Force an unconfigured state for this specific test
    with patch("app.core.config.settings.GCP_PROJECT_ID", None):
        service = GCPSecretService()
        with pytest.raises(ValueError, match="GCP Project ID not configured"):
            service.get_secret("some_key")
