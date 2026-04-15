from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum

class Status(str, Enum):
    open = "open"
    in_progress = "in_progress"
    done = "done"

class Priority(str, Enum):
    High = "high"
    Medium = "medium"
    Low = "low"

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: Optional[Priority] = Priority.Medium
    due_date: Optional[datetime] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: Status
    priority: Priority
    due_date: Optional[datetime]
    created_at: datetime

class TaskUpdate(BaseModel):
    description: Optional[str] = None
    status: Optional[Status] = None
    priority: Optional[Priority] = None
    due_date: Optional[datetime] = None

    # This allows Pydantic to read data from SQLAlchemy models directly
    model_config = {"from_attributes": True}

