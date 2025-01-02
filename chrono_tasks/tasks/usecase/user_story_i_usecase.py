from abc import ABC, abstractmethod
from tasks.usecase.user_story_dto import UserStoryInputDTO
from tasks.domain.user_story_i_repository import UserStoryIRepository

class UserStoryIUseCase(ABC):
    @abstractmethod
    def __init__(self, epic_repository: UserStoryIRepository) -> None:
        raise NotImplementedError

    @abstractmethod
    def create_user_story(self, epic_input: UserStoryInputDTO):
        raise NotImplementedError