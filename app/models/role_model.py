"""Role Model defines the database model structure for role module."""
from sqlalchemy import Column, Integer, String, text

from app.config.database.base_class import Base
from app.utils.datetime_custom_type import CustomDateTime


class Role(Base):
    """Role database model."""
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_at = Column(CustomDateTime,
                        nullable=False,
                        server_default=text("CURRENT_TIMESTAMP"))

    def __repr__(self) -> str:
        return (f'<{self.id},'
                f'{self.name}'
                )
