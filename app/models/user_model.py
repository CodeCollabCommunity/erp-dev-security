"""User Model defines the database model structure for user module."""
from sqlalchemy import Column, String, Integer, text, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database.base_class import Base
from app.utils.datetime_custom_type import CustomDateTime


class User(Base):
    """User database model."""
    id = Column(Integer, primary_key=True, index=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey("role.id"), nullable=True)
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
