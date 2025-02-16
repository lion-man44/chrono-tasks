from tasks.domain.epic_i_repository import EpicIRepository

from tasks.usecase.epic_dto import EpicInputDTO
from tasks.domain.epic_entity import EpicEntity
from tasks.models import Epic

class EpicRepository(EpicIRepository):
  def save(self, epic_input_dto: EpicInputDTO) -> EpicEntity:
    epic = EpicEntity(epic_input_dto)
    Epic.objects.update_or_create(defaults=epic)
    return epic.model_validate()