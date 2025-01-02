from abc import ABC, abstractmethod

class EpicIRepository(ABC):
    @abstractmethod
    def save(self, epic):
        pass

    @abstractmethod
    def find_by_id(self, id):
        pass

    @abstractmethod
    def find_user_stories(self, id):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def delete(self, epic):
        pass

    @abstractmethod
    def update(self, epic):
        pass