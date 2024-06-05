from typing import Generator

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from sqlalchemy import create_engine
# from sqlalchemy.orm import as_declarative, declared_attr, declarative_base
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.pool import StaticPool

from app.config.database.base_class import Base
from app.helpers.db import get_db
from app.main import app as fastapi_app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
SQLALCHEMY_DATABASE_POSTGRESQL_URL = "postgresql://postgres:postgres@db2:5433/postgres"
"""
Setup sqlite db for tests
"""
# Base = declarative_base()

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
# engine = create_engine(
#     SQLALCHEMY_DATABASE_POSTGRESQL_URL,
#     isolation_level="REPEATABLE READ"
# )

TestingSessionLocal = scoped_session(sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    ))


Base.metadata.create_all(bind=engine)


@pytest.fixture(scope="session")
def db() -> Generator:
    """
    Get db session for tests
    """
    session = TestingSessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)


def override_get_db():
    """
    Override get_db dependency
    """
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


def override_validate_token():
    """override_validate_token"""
    return None


@pytest.fixture(scope="module")
def client() -> Generator:
    """Override test client with local db

    Yields:
        Generator: TestClient
    """
    fastapi_app.dependency_overrides[get_db] = override_get_db
    # fastapi_app.dependency_overrides[validate_token] = override_validate_token

    yield TestClient(fastapi_app)


@pytest.fixture(scope="module")
def async_client() -> Generator:
    """Override test client with local db

    Yields:
        Generator: TestClient
    """
    fastapi_app.dependency_overrides[get_db] = override_get_db
    # fastapi_app.dependency_overrides[validate_token] = override_validate_token

    yield AsyncClient(app=fastapi_app, base_url="http://test")
