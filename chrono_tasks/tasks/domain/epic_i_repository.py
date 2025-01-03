from abc import ABC, abstractmethod
from tasks.usecase.epic_dto import EpicListInputDTO, EpicInputDTO
from tasks.domain.type import EpicId

class EpicIRepository(ABC):
    @abstractmethod
    def save(self, epic_input_dto: EpicInputDTO):
        pass

    @abstractmethod
    def find_by_id(self, id: EpicId):
        pass

    @abstractmethod
    def find_user_stories_by_id(self, id: EpicId):
        pass

    @abstractmethod
    def list(self, epic_list_input_dto: EpicListInputDTO):
        pass

    @abstractmethod
    def delete(self, epic_input_dto: EpicInputDTO):
        pass