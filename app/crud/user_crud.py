"""
Generate an Object of CRUD for users
"""
from typing import Any

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.config.database.crud_base import CRUDBase
from app.models.user_model import User as UserModel
from app.schemas.user_schema import UserCreateSchema, UserUpdateSchema
from app.auth.services import get_password_hash

class CRUDUser(CRUDBase[UserModel, UserCreateSchema, UserUpdateSchema]):
    """User CRUD class
    Args:
        CRUDBase ([Item, ItemCreate, ItemUpdate])
    """
    def create(self, db: Session, obj_in: UserCreateSchema | dict[str, Any]) -> UserModel:
        """Create a ModelType object"""
        obj_in_data = jsonable_encoder(obj_in)
        obj_in_data['password'] = get_password_hash(obj_in_data['password'])
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_email(self, email: str, db: Session) -> UserModel:
        """Return user object matched by email"""
        return db.query(self.model).filter(self.model.email == email).first()


user_crud = CRUDUser(UserModel)
