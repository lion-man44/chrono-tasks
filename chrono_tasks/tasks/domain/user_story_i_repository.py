from abc import ABC, abstractmethod

from tasks.usecase.user_story_dto import UserStoryInputDTO, UserStoryListInputDTO
from tasks.domain.type import UserStoryId

class UserStoryIRepository(ABC):
    @abstractmethod
    def save(self, user_story_input_dto: UserStoryInputDTO):
        pass

    @abstractmethod
    def find_by_id(self, id: UserStoryId):
        pass

    @abstractmethod
    def find_tasks_by_id(self, id: UserStoryId):
        pass

    @abstractmethod
    def list(self, user_story_list_input_dto: UserStoryListInputDTO):
        pass

    @abstractmethod
    def delete(self, user_story_input_dto: UserStoryInputDTO):
        pass