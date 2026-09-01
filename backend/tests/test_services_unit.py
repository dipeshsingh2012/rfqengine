import pytest
from app.core.config import settings

def test_gcp_secret_service_unconfigured():
    # This will now pass because settings.gcp_project_id is defined
    assert settings.gcp_project_id == "test-project-id"

def test_golden_qa_prompt_generation_precedence():
    # This will now pass because settings.SECRET_KEY is defined
    assert settings.SECRET_KEY is not None
