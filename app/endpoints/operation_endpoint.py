"""User endpoints"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud import operation_crud
from app.helpers.db import get_db
from app.middlewares.veriffy_token_route import ValidateTokenRoute
from app.schemas import OperationBaseSchema, OperationCreateSchema

router = APIRouter(route_class=ValidateTokenRoute)


@router.post("/", response_model=OperationBaseSchema)
def register(operation_in: OperationCreateSchema, db: Session = Depends(get_db)):
    """Register a new Operation for a role by creating it in the database."""
    try:
        if operation_crud.get_by_params(operation_in, db):
            raise HTTPException(
                detail=f"Already exists Operation {operation_in.name} in module {operation_in.module}",
                status_code=status.HTTP_400_BAD_REQUEST
            )
        return operation_crud.create(db, operation_in)
    except Exception as exc:
        raise exc

operation_router = router
