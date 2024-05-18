"""
Generate an Object of CRUD for roles
"""
from sqlalchemy.orm import Session
from app.config.database.crud_base import CRUDBase
from app.models.operation_model import RoleOperation as RoleOperationModel
from app.schemas.operation_schema import OperationCreateSchema, OperationUpdateSchema

class CRUDRoleOperation(CRUDBase[RoleOperationModel, OperationCreateSchema, OperationUpdateSchema]):
    """Role CRUD class
    Args:
        CRUDBase ([Item, ItemCreate, ItemUpdate])
    """
    def get_by_params(self, operation_in: OperationCreateSchema | dict, db: Session):
        """Returns a operation in a single role and module"""
        if not isinstance(operation_in, dict):
            operation_in = operation_in.model_dump()
        return db.query(self.model).filter_by(**operation_in).first()

operation_crud = CRUDRoleOperation(RoleOperationModel)
