"""User Model defines the database model structure for user module."""
from uuid import uuid4

from sqlalchemy import UUID, Column, ForeignKey, String, text
from sqlalchemy.orm import relationship

from app.config.database.base_class import Base
from app.utils.datetime_custom_type import CustomDateTime


class User(Base):
    """User database model."""
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    role_id = Column(UUID(as_uuid=True), ForeignKey("role.id"), nullable=True)
    created_at = Column(CustomDateTime,
                        nullable=False,
                        server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(CustomDateTime,
                        nullable=False,
                        server_default=text("CURRENT_TIMESTAMP"))

    user_role = relationship("UserRoles", back_populates="user")
    def __repr__(self) -> str:
        return (f'<{self.id},'
                f'{self.email}'
                f'{self.role_id}'
                )
