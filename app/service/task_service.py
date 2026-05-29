from datetime import datetime

from converter.task_converter import to_creation_entity, to_dto
from dto.task_creation_dto import TaskCreationDTO
from dto.task_dto import TaskDTO
from repository.task_repository import TaskRepository


class TaskService:
    def create_task(self, db, dto: TaskCreationDTO) -> TaskDTO:
        task = to_creation_entity(dto)
        repository = TaskRepository(db)
        repository.save_task(task)
        return to_dto(task)

    def update_task(self, db, task_id: int, dto: TaskCreationDTO) -> TaskDTO:
        repository = TaskRepository(db)

        task = repository.get_task_by_id(task_id)
        if not task:
            return None

        task.title = dto.title
        task.description = dto.description
        task.status = dto.status
        task.updated_at = datetime.utcnow()

        repository.save_task(task)

        return to_dto(task)

    def get_all_tasks(self, db, status=None) -> list[TaskDTO]:
        repository = TaskRepository(db)
        tasks = repository.get_all_tasks(status)
        return [to_dto(task) for task in tasks]

    def get_task_by_id(self, db, id: int) -> TaskDTO:
        repository = TaskRepository(db)
        task = repository.get_task_by_id(id)
        if not task:
            return None
        return to_dto(task)

    def delete_task(self, db, task_id: int) -> bool:
        repository = TaskRepository(db)
        return repository.delete_task(task_id)
