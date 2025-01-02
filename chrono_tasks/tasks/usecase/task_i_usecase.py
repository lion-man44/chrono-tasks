from abc import ABC, abstractmethod
from tasks.usecase.task_dto import TaskInputDTO
from tasks.domain.task_i_repository import TaskIRepository

class TaskIUseCase(ABC):
    @abstractmethod
    def __init__(self, epic_repository: TaskIRepository) -> None:
        raise NotImplementedError

    @abstractmethod
    def create_task(self, epic_input: TaskInputDTO):
        raise NotImplementedError