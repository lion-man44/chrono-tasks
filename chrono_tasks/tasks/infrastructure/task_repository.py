from tasks.domain.task_i_repository import TaskIRepository

from tasks.usecase.task_dto import TaskInputDTO
from tasks.domain.task_entity import TaskEntity
from tasks.models import Task

class TaskRepository(TaskIRepository):
  def save(self, task_input_dto: TaskInputDTO) -> TaskEntity:
    task = TaskEntity(task_input_dto)
    Task.objects.update_or_create(defaults=task)
    return task.model_validate()