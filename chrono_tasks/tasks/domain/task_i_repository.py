from abc import ABC, abstractmethod

from tasks.domain.type import TaskId
from tasks.usecase.task_dto import TaskInputDTO, TaskListInputDTO

class TaskIRepository(ABC):
    @abstractmethod
    def save(self, task_input_dto: TaskInputDTO):
        pass

    @abstractmethod
    def find_by_id(self, id: TaskId):
        pass

    @abstractmethod
    def find_ancestors_by_id(self, id: TaskId):
        pass

    @abstractmethod
    def list(self, task_list_input_dto: TaskListInputDTO):
        pass

    @abstractmethod
    def delete(self, task_input_dto: TaskInputDTO):
        pass
