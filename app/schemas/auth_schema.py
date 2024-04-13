"""User schema module for user data serialization."""
from pydantic import BaseModel, EmailStr


class UserAuthSchema(BaseModel):
    """Define the schema for user authentication data."""
    email: EmailStr
    password: str


class Token(BaseModel):
    """Define the schema for user token."""
    access_token: str
    token_type: str
