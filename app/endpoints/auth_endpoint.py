"""User endpoints"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.services import generate_token
from app.helpers.db import get_db
from app.schemas import Token, UserAuthSchema

router = APIRouter()


@router.get('/login/', description='Sign-in.', response_model=Token)
def login_for_access_token(authenticate: UserAuthSchema, db: Session = Depends(get_db)):
    """Returns The generated access token."""
    access_token = generate_token(db=db, email=authenticate.email, password=authenticate.password)
    return Token(access_token=access_token, token_type="bearer")

auth_router = router
