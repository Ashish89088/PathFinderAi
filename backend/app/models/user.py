import uuid
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from .base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    age = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())