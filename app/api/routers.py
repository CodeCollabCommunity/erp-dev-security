from fastapi import APIRouter

from app.endpoints import auth_router, role_router, user_router

api_router = APIRouter()

api_router.include_router(
    router=auth_router,
    prefix='/auth',
    tags=['auth'],
    responses={418: {'description': 'I"m a teapot =)'}}
)

api_router.include_router(
    router=user_router,
    prefix='/users',
    tags=['users'],
    responses={418: {'description': 'I"m a teapot =)'}}
)

api_router.include_router(
    router=role_router,
    prefix='/roles',
    tags=['roles'],
    responses={418: {'description': 'I"m a teapot =)'}}
)
