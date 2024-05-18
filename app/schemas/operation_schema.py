"""Operation schema module for operation data serialization."""
from typing import ClassVar
from uuid import UUID

from pydantic import BaseModel, Field, model_validator


class OperationBaseSchema(BaseModel):
    """Define the schema for a Operation object."""
    id: UUID
    name: str = Field(min_length=3)
    module: str


class OperationCreateSchema(OperationBaseSchema):
    """Define the create schema for a Operation object."""
    id: ClassVar
    role_id: UUID

    @model_validator(mode="before")
    def standarize_fields(self):
        """set to upper case fields."""
        for field, value in self.items():
            if isinstance(value, str):
                self[field] = value.strip().replace(" ", "_").upper()
        return self

class OperationUpdateSchema(OperationBaseSchema):
    """Define the update schema for a Operation object."""


class OperationRequestSchema(OperationBaseSchema):
    """Define the schema for a Operation request."""
    id: ClassVar
    role_id: UUID | None = None
