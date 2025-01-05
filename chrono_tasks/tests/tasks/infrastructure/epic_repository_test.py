from uuid import uuid4
from datetime import datetime
import pytest

from tasks.usecase.epic_dto import EpicInputDTO
from tasks.domain.type import CreatedByUserId, EpicId
from tasks.domain.epic_entity import EpicEntity

class TestEpicRepository:
    class InMemoryRepository:
        id: EpicId
        display_id: int
        name: str
        content: str
        started_at: datetime
        opened_merge_request_at: datetime
        ended_at: datetime
        created_at: datetime
        updated_at: datetime
        created_by_user_id: CreatedByUserId

        def save(self, epic_input_dto: EpicInputDTO) -> EpicEntity:
            epic = EpicEntity(**epic_input_dto)
            return epic.model_validate(epic)

    class TestSave:
        @pytest.fixture
        def epic_fixture(self):
            return {
                'display_id': 1,
                'name': 'Epic 1',
                'content': 'Content of Epic 1',
                'started_at': datetime.now(),
                'opened_merge_request_at': datetime.now(),
                'ended_at': datetime.now(),
                'created_at': datetime.now(),
                'updated_at': datetime.now(),
                'created_by_user_id': uuid4()
            }

        def test_return_epic_entity_when_creating_an_epic(self, epic_fixture):
            repository = TestEpicRepository.InMemoryRepository()
            epic = repository.save(epic_fixture)
            assert isinstance(epic, EpicEntity)
            assert epic.display_id == 1
            assert epic.name == 'Epic 1'
            assert epic.content == 'Content of Epic 1'


        def test_update_an_epic(self):
            pass