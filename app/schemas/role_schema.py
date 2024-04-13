"""Role schema module for role data serialization."""
from pydantic import BaseModel, Field, field_validator


class RoleBaseSchema(BaseModel):
    """Define the schema for a Role object."""
    id: int
    name: str = Field(min_length=3)


class RoleCreateSchema(BaseModel):
    """Define the create schema for a Role object."""
    name: str = Field(min_length=3)

    @field_validator("name")
    @classmethod
    def parse_name(cls, value):
        """Returns upper case role name."""
        return value.strip().replace(" ", "_").upper()


class RoleUpdateSchema(BaseModel):
    """Define the update schema for a Role object."""
    name: str = Field(min_length=3)
