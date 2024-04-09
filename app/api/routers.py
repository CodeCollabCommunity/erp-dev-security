"""API Routes Mdule"""
from fastapi import APIRouter
from app.endpoints import user_router


api_router = APIRouter()

api_router.include_router(
    router=user_router,
    prefix='/users',
    tags=['users'],
    responses={418: {'description': 'I"m a teapot =)'}}
)
