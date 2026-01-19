import uuid
from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from .base import Base

class CareerAnalysis(Base):
    __tablename__ = "career_analyses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    inferred_traits = Column(JSONB)
    career_recommendations = Column(JSONB)
    roadmaps = Column(JSONB)
    opportunities = Column(JSONB)
    raw_ai_output = Column(JSONB)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
