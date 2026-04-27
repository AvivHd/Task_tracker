from sqlalchemy import Column, Integer, String, DateTime
import enum
from sqlalchemy.sql import func
from app.database import Base

class Status(str, enum.Enum):
    open = "open"
    in_progress = "in_progress"
    done = "done"

class Priority(str, enum.Enum):
    high = "high"
    medium = "medium"
    low = "low"

class Task(Base):
    __tablename__ = "Tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(String, default="open")
    priority = Column(String, default="medium")
    due_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=func.now())