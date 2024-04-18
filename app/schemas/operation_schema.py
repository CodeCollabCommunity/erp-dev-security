"""Operation schema module for operation data serialization."""
from typing import ClassVar
from pydantic import BaseModel, Field,  model_validator


class OperationBaseSchema(BaseModel):
    """Define the schema for a Operation object."""
    id: int
    name: str = Field(min_length=3)
    module: str


class OperationCreateSchema(OperationBaseSchema):
    """Define the create schema for a Operation object."""
    id: ClassVar
    role_id: int

    @model_validator(mode="before")
    def standarize_fields(self):
        """set to upper case fields."""
        for field, value in self.items():
            if isinstance(value, str):
                self[field] = value.strip().replace(" ", "_").upper()
        return self

class OperationUpdateSchema(OperationBaseSchema):
    """Define the update schema for a Operation object."""
