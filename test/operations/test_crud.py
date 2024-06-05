"""
Module for testing the crud functionality of the role' app.
"""
import pytest
from pytest import fixture
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.crud import role_crud
from app.schemas import RoleCreateSchema

from .mocks import role_in, role_in_fixture


def test_crud_create_operation(db: Session) -> None:
    """
    Test create CRUD method
    """
    _role_in = RoleCreateSchema(**role_in)
    role_created = role_crud.create(db=db, obj_in=_role_in)

    assert role_created.name == _role_in.name

def test_crud_get_operation(create_role: fixture, db: Session) -> None:
    """
    Test get CRUD method
    """
    role_id = create_role.id
    role_name = create_role.name
    role_retrieved = role_crud.get(id=role_id, db=db)

    assert role_id == role_retrieved.id
    assert role_name == role_retrieved.name

@pytest.fixture
def create_role(client: TestClient, db: Session):
    """Fixture for role creation."""
    role = RoleCreateSchema(**role_in_fixture)
    return role_crud.create(db=db, obj_in=role)
