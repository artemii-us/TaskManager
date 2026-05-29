from database.db import get_connection
from dto.task_creation_dto import TaskCreationDTO
from dto.task_dto import TaskStatus
from fastapi import APIRouter, Depends, Query
from service.task_service import TaskService
from sqlalchemy.orm import Session

router = APIRouter()
task_service = TaskService()


@router.get("/tasks")
def get_all_tasks(
    db: Session = Depends(get_connection),
    status: TaskStatus | None = Query(default=None),
):
    return task_service.get_all_tasks(db=db, status=status)


@router.post("/tasks")
def create_task(task: TaskCreationDTO, db: Session = Depends(get_connection)):
    return task_service.create_task(db=db, dto=task)


@router.patch("/tasks/{task_id}")
def update_task(
    task_id: int, task: TaskCreationDTO, db: Session = Depends(get_connection)
):
    return task_service.update_task(db=db, task_id=task_id, dto=task)


@router.get("/tasks/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_connection)):
    task = task_service.get_task_by_id(db=db, id=task_id)
    if not task:
        return {"error": "Task not found"}
    return task


@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_connection)):
    res = task_service.delete_task(db=db, task_id=task_id)
    if not res:
        return {"error": "Task not found"}
    return {"message": "Task deleted successfully"}
