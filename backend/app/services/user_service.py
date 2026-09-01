from typing import Any, Dict, Optional, List
from app.core.config import settings

class UserService:
    """Service handling user-related business logic."""
    
    def __init__(self):
        self.project_context = settings.PROJECT_NAME

    async def get_user_by_id(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Fetch a user by their unique identifier."""
        # Mock implementation for demonstration
        if user_id == "error":
            return None
        return {"id": user_id, "name": "Test User", "context": self.project_context}

    async def list_users(self) -> List[Dict[str, Any]]:
        """List all users."""
        return [{"id": "1", "name": "Alice"}, {"id": "2", "name": "Bob"}]
