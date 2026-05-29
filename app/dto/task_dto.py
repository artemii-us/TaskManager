from datetime import datetime

from models.task_enum import TaskStatus
from pydantic import BaseModel, Field


class TaskDTO(BaseModel):
    id: int
    title: str = Field(min_length=1, max_length=255)
    description: str = Field(min_length=1, max_length=511)
    status: TaskStatus
    created_at: datetime
    updated_at: datetime
