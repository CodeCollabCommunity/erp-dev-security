"""User schema module for user data serialization."""
from typing import ClassVar

from fastapi import HTTPException, status
from pydantic import (BaseModel, EmailStr, Field,
                      field_validator)

from app.auth.services import validate_password


class UserBaseSchema(BaseModel):
    """User base schema class."""
    email: EmailStr = Field(examples=['Some@Some.Some'])
    role_id: int | None = None
    password: str = Field(min_length=5, max_length=15)


class UserCreateSchema(UserBaseSchema):
    """Schema class for user creation."""

    @field_validator("password")
    @classmethod
    def validate_passwords(cls, password):
        """Validate password rules."""
        if not validate_password(password):
            raise HTTPException(
                detail="The password must have 5 to 15 characters, 1 uppercase letter, 1 lowercase,"
                "letter, 1 number, 1 special character (! @ # $ % & * . _), and must not contain spaces.",
                status_code=status.HTTP_400_BAD_REQUEST
            )
        return password


class UserUpdateSchema(UserBaseSchema):
    """Schema class for user update."""
    email: EmailStr | None = None
    role_id: int | None = None
    password: str | None = None
    re_password: str | None = None


class UserResponseSchema(UserBaseSchema):
    """Schema class for responses."""
    password: ClassVar[str]


class UserListResponseSchema(BaseModel):
    data: list[UserBaseSchema]
    # password: ClassVar[str]


class Token(BaseModel):
    access_token: str
    token_type: str


class UserAuthSchema(BaseModel):
    username: str
    password: str


class UserInDBSchema(UserBaseSchema):
    password: ClassVar[str]

    class Config:
        """
        Use SQLAlchemy to Pydantic
        """
        from_attributes = True


class UsersInDBSchema(BaseModel):
    usuarios: list[UserBaseSchema]
    # password: ClassVar[str]

    class Config:
        """
        Use SQLAlchemy to Pydantic
        """
        from_attributes = True
