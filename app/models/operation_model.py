"""RoleOperation Model defines the database model structure for role operation module."""
from uuid import uuid4

from sqlalchemy import UUID, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.config.database.base_class import Base
from app.utils.datetime_custom_type import CustomDateTime


class RoleOperation(Base):
    """Operation database model."""
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    name = Column(String, nullable=False)
    module = Column(String, nullable=False)
    role_id = Column(UUID(as_uuid=True), ForeignKey("role.id"), nullable=False)
    #TODO
    # relationship to user
    def __repr__(self) -> str:
        return (f'<{self.id},'
                f'{self.name}'
                f'{self.module}'
                )
