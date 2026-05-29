from datetime import datetime

from database.base import Base
from models.task_enum import TaskStatus
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy import Enum as SAEnum


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String(511), nullable=False)
    status = Column(SAEnum(TaskStatus), nullable=False, default=TaskStatus.new)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)
