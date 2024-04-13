import os
import re
from datetime import timedelta, datetime
from typing import Any

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def validate_password(password: str) -> Any:
    """The result of matching the password against the regex pattern."""
    regex = re.compile(
        r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%&*._])(?!.*\s).{5,15}$"
    )
    return re.fullmatch(regex, password)


def get_password_hash(plain_password):
    """Returns password hashed."""
    return pwd_context.hash(plain_password)
