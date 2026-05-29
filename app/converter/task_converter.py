from dto.task_creation_dto import TaskCreationDTO
from dto.task_dto import TaskDTO
from models.task import Task


def to_creation_entity(dto: TaskCreationDTO) -> Task:
    return Task(
        title=dto.title,
        description=dto.description,
        status=dto.status,
    )


def to_dto(task: Task) -> TaskDTO:
    return TaskDTO(
        id=task.id,
        title=task.title,
        description=task.description,
        status=task.status,
        created_at=task.created_at,
        updated_at=task.updated_at,
    )


def to_entity(dto: TaskDTO) -> Task:
    return Task(
        id=dto.id,
        title=dto.title,
        description=dto.description,
        status=dto.status,
        created_at=dto.created_at,
        updated_at=dto.updated_at,
    )
