from abc import ABC, abstractmethod

class TaskIRepository(ABC):
    @abstractmethod
    def save(self, task):
        pass

    @abstractmethod
    def find_by_id(self, id):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def delete(self, task):
        pass

    @abstractmethod
    def update(self, task):
        pass

    @abstractmethod
    def find_ancestors(self, task):
        pass