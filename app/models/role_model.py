"""Role Model defines the database model structure for role module."""
from uuid import uuid4
from sqlalchemy import Column, Integer, String, text, UUID
from sqlalchemy.orm import relationship
from app.config.database.base_class import Base
from app.utils.datetime_custom_type import CustomDateTime


class Role(Base):
    """Role database model."""
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    name = Column(String, nullable=False)
    created_at = Column(CustomDateTime,
                        nullable=False,
                        server_default=text("CURRENT_TIMESTAMP"))

    user_role = relationship("UserRoles", back_populates="role")
    def __repr__(self) -> str:
        return (f'<{self.id},'
                f'{self.name}'
                )
