"""User endpoints"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.services import get_current_user
from app.crud import operation_crud, role_crud
from app.helpers.db import get_db
from app.middlewares.veriffy_token_route import ValidateTokenRoute
from app.models import User
from app.schemas import (OperationBaseSchema, OperationCreateSchema,
                         OperationRequestSchema)

router = APIRouter(route_class=ValidateTokenRoute)


@router.post("/", response_model=OperationBaseSchema)
def register(operation_in: OperationCreateSchema, db: Session = Depends(get_db)):
    """Register a new Operation for a role by creating it in the database."""
    try:
        role_id = operation_in.role_id
        if not role_crud.get(role_id, db):
            raise HTTPException(
                detail="Role does not exists.",
                status_code=status.HTTP_400_BAD_REQUEST
            )
        if operation := operation_crud.get_by_params(operation_in, db):
            raise HTTPException(
                detail=f"Already exists Operation {operation.name} in module {operation.module}",
                status_code=status.HTTP_400_BAD_REQUEST
            )
        return operation_crud.create(db, operation_in)
    except Exception as exc:
        raise exc


@router.post("/authorization", status_code=200)
def authorize_operation(operation: OperationRequestSchema,
                        current_user: User = Depends(get_current_user),
                        db: Session = Depends(get_db)):
    """Endpoint to authorize users operations in ERP modules."""
    operation.role_id = current_user.role_id

    if user_authorization := operation_crud.get_by_params(operation, db):
        # TODO implementar esta seccion
        return True
    raise HTTPException(
        detail= "User is unable to do that operation or doesn't exist.",
        status_code= status.HTTP_401_UNAUTHORIZED
    )


operation_router = router
