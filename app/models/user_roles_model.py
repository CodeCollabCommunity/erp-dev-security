"""UserRoles Model defines the database model structure for User roles module."""
from sqlalchemy import Column, Integer, text, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database.base_class import Base
from app.utils.datetime_custom_type import CustomDateTime


class UserRoles(Base):
    """User_roles database model."""
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    role_id = Column(Integer, ForeignKey("role.id"), nullable=True)
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
