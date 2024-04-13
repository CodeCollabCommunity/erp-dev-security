"""
Generate an Object of CRUD for roles
"""
from sqlalchemy.orm import Session
from app.config.database.crud_base import CRUDBase
from app.models.role_model import Role as RoleModel
from app.schemas.role_schema import RoleCreateSchema, RoleUpdateSchema

class CRUDRole(CRUDBase[RoleModel, RoleCreateSchema, RoleUpdateSchema]):
    """Role CRUD class
    Args:
        CRUDBase ([Item, ItemCreate, ItemUpdate])
    """
    def get_by_name(self, role_name: str, db: Session) -> RoleModel:
        """Retrieve a Role by its name from the database."""
        return db.query(self.model).filter(self.model.name == role_name).first()

role_crud = CRUDRole(RoleModel)
