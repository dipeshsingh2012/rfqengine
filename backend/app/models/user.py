from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    email: str = Field(..., description="User email address")
    name: str = Field(..., description="User full name")
