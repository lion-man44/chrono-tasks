from abc import ABC, abstractmethod
from tasks.usecase.epic_dto import EpicListInputDTO, EpicInputDTO
from tasks.domain.type import EpicId
from tasks.domain.epic_entity import EpicEntity
from tasks.domain.user_story_entity import UserStoryEntity

class EpicIRepository(ABC):
    @abstractmethod
    def save(self, epic_input_dto: EpicInputDTO) -> EpicEntity:
        pass

    @abstractmethod
    def find_by_id(self, id: EpicId) -> EpicEntity:
        pass

    @abstractmethod
    def find_user_stories_by_id(self, id: EpicId) -> UserStoryEntity[list]:
        pass

    @abstractmethod
    def list(self, epic_list_input_dto: EpicListInputDTO) -> EpicEntity[list]:
        pass

    @abstractmethod
    def delete(self, epic_input_dto: EpicInputDTO) -> EpicEntity:
        pass