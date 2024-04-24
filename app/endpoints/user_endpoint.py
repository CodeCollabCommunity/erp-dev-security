"""User endpoints"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud import user_crud
from app.helpers.db import get_db
from app.schemas import UserCreateSchema, UserResponseSchema
from app.middlewares.veriffy_token_route import ValidateTokenRoute

router = APIRouter(route_class=ValidateTokenRoute)


@router.post("/", response_model=UserResponseSchema)
def register(user_in: UserCreateSchema, db: Session = Depends(get_db)):
    """Register a new User by creating it in the database."""
    try:
        email = user_in.email
        if user_crud.get_by_email(email, db):
            raise HTTPException(
                detail=f"Already exists email {email} registered.",
                status_code=status.HTTP_400_BAD_REQUEST
            )
        return user_crud.create(db, user_in)
    except Exception as exc:
        raise exc


user_router = router
