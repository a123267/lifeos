from sqlalchemy import Column, Integer, String, DateTime, JSON
from sqlalchemy.sql import func

from backend.app.database import Base


class ActivityEvent(Base):
    __tablename__ = "activity_events"

    id = Column(Integer, primary_key=True, index=True)
    entity_type = Column(String(50), nullable=False)
    entity_id = Column(Integer, nullable=False)
    event_type = Column(String(50), nullable=False)
    event_data = Column(JSON, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
