"""CRUD BASE module"""
from typing import Any, Generic, List, Type, TypeVar

from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorClient

from .base_class import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar('CreateSchemaType', bound=Base)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=Base)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        Args:

        `model`: A SQLAlchemy model class
        `schema`: A Pydantic model (schema) class
        """
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def create(self, db: AsyncIOMotorClient, obj_in: CreateSchemaType | dict[str, Any]) -> ModelType:
        """Create a ModelType object"""
        obj_in_data = obj_in if isinstance(obj_in, dict) else obj_in.model_dump()
        model_obj = self.model(**obj_in_data)
        db_obj = jsonable_encoder(model_obj)
        db_obj = await db.collection.insert_one(db_obj)
        inserted_obj = await db.collection.find_one({"id": db_obj.inserted_id})
        return inserted_obj

    async def update(self, db: AsyncIOMotorClient, obj_in: UpdateSchemaType | dict[str, Any], db_obj: ModelType) -> ModelType:
        """Update a ModelType object"""
        obj_in_data = obj_in if isinstance(obj_in, dict) else obj_in.model_dump()
        model_object = jsonable_encoder(db_obj)

        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_none=True)
        for field in obj_in_data:
            if field in update_data:
                setattr(model_object, field, update_data[field])
        db_obj = await db.collection.update_one({"_id": db_obj["_id"]}, {"$set": model_object})
        updated_obj = await db.collection.find_one({"_id": db_obj.inserted_id})
        return updated_obj

    def get(self, object_id: str, db: AsyncIOMotorClient) -> ModelType:
        """Get a single ModelType filtered by object_id"""
        return db.collection.find_one({"_id": object_id})

    def get_multi(self, db: AsyncIOMotorClient) -> List[ModelType]:
        """Get al ModelTypes objects"""
        return db.collection.find({self.model})
