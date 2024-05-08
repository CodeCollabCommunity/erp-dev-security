from uuid import UUID
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from typing import Generic, TypeVar, Type, Any, List
from .base_class import Base

ModelType = TypeVar('ModelType', bound=Base)
CreateSchemaType = TypeVar('CreateSchemaType', bound=Base)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=Base)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        Args:

        `model`: A SQLAlchemy model class
        `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def create(self, db: Session, obj_in: CreateSchemaType | dict[str, Any]) -> ModelType:
        """Create a ModelType object"""
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, obj_in: CreateSchemaType | dict[str, Any], db_obj: ModelType) -> ModelType:
        """Update a ModelType object"""
        obj_in_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_none=True)
        for field in obj_in_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get(self, id: int | UUID, db: Session) -> ModelType:
        """Get a single ModelType filtered by id"""
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(self, db: Session) -> List[ModelType]:
        """Get al ModelTypes objects"""
        return db.query(self.model).all()
