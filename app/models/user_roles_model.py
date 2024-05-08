"""UserRoles Model defines the database model structure for User roles module."""
from uuid import uuid4

from sqlalchemy import UUID, Column, ForeignKey, Integer, text
from sqlalchemy.orm import relationship

from app.config.database.base_class import Base
from app.utils.datetime_custom_type import CustomDateTime


class UserRoles(Base):
    """User_roles database model."""
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=False)
    role_id = Column(UUID(as_uuid=True), ForeignKey("role.id"), nullable=True)
    created_at = Column(CustomDateTime,
                        nullable=False,
                        server_default=text("CURRENT_TIMESTAMP"))

    user = relationship("User", back_populates="user_role")
    role = relationship("Role", back_populates="user_role")
    def __repr__(self) -> str:
        return (f'<{self.id},'
                f'{self.user_id}'
                f'{self.role_id}'
                )
