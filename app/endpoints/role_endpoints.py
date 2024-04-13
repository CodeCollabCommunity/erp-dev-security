"""User endpoints"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud import role_crud
from app.helpers.db import get_db
from app.schemas import RoleBaseSchema, RoleCreateSchema

router = APIRouter()


@router.post("/", response_model=RoleBaseSchema)
def register(role_in: RoleCreateSchema, db: Session = Depends(get_db)):
    """Register a new Role by creating it in the database."""
    try:
        role_name = role_in.name
        if role_crud.get_by_name(role_name, db):
            raise HTTPException(
                detail=f"Already exists role with name: {role_name}",
                status_code=status.HTTP_400_BAD_REQUEST
            )
        return role_crud.create(db, role_in)
    except Exception as exc:
        raise exc

role_router = router
