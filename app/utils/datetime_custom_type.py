"""
Custom datetime type for SQLAlchemy.
"""

import pendulum
from sqlalchemy import DateTime, TypeDecorator


class CustomDateTime(TypeDecorator):
    """DateTime decorator

    Returns:
        [pendulum.datetime]: datetime from string
    """
    cache_ok = True
    impl = DateTime

    def process_bind_param(self, value, dialect):
        """
        Process bind param
        """
        if type(value) is str:
            return pendulum.from_format(value, "YYYY-MM-DDTHH:mm:ss.SSSSSS[Z]")
        return value
