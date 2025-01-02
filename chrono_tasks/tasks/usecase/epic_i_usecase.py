from abc import ABC, abstractmethod
from tasks.usecase.epic_dto import EpicInputDTO
from tasks.domain.epic_i_repository import EpicIRepository

class EpicIUseCase(ABC):
    @abstractmethod
    def __init__(self, epic_repository: EpicIRepository) -> None:
        # self.epic_repository = epic_repository
        raise NotImplementedError

    @abstractmethod
    def create_epic(self, epic_input: EpicInputDTO):
        raise NotImplementedError
        # epic = EpicEntity(epic_input)
        # self.epic_repository.save(epic)
        # return epic.model_validate()