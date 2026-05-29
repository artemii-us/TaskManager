from enum import Enum


class TaskStatus(Enum):
    new = "new"
    in_progress = "in_progress"
    done = "done"
