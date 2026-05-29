from models.task import Task


class TaskRepository:
    def __init__(self, session):
        self.session = session

    def get_all_tasks(self, status=None) -> list[Task]:
        if status is None:
            return self.session.query(Task).all()
        return self.session.query(Task).filter_by(status=status).all()

    def get_task_by_id(self, id: int) -> Task:
        return self.session.query(Task).filter_by(id=id).first()

    def save_task(self, task: Task):
        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)
        return task

    def delete_task(self, task_id: int) -> bool:
        task = self.session.get(Task, task_id)
        if not task:
            return False

        self.session.delete(task)
        self.session.commit()
        return True
