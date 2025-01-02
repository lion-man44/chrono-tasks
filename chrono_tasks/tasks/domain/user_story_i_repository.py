from abc import ABC, abstractmethod

class UserStoryIRepository(ABC):
    @abstractmethod
    def save(self, user_story):
        pass

    @abstractmethod
    def find_by_id(self, id):
        pass

    @abstractmethod
    def find_tasks(self, id):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def delete(self, user_story):
        pass

    @abstractmethod
    def update(self, user_story):
        pass