import uuid
from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from .base import Base

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    academics = Column(JSONB)
    interests = Column(JSONB)
    hobbies = Column(JSONB)
    platforms = Column(JSONB)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
