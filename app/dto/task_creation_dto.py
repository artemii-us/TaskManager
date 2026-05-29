from models.task_enum import TaskStatus
from pydantic import BaseModel, Field


class TaskCreationDTO(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    description: str = Field(min_length=1, max_length=511)
    status: TaskStatus
