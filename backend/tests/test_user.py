import pytest
from app.models.user import UserSchema

def test_user_schema_valid():
    user = UserSchema(email="test@example.com", name="Test User")
    assert user.email == "test@example.com"
    assert user.name == "Test User"
