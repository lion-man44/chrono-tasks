import pytest
from django.utils import timezone
from freezegun import freeze_time


from tasks.infrastructure.user_story_repository import UserStoryRepository
from tasks.usecase.user_story_dto import UserStoryInputDTO
from tasks.models import Epic
from users.models import User

class TestUserStoryRepository:
    class TestSave:
        @pytest.fixture
        @freeze_time('2021-01-01')
        def user_story_input_dto_fixture(self, user_fixture):
            epic = Epic.objects.create(
                display_id=1,
                name='Epic 1',
                content='Content of Epic 1',
                started_at=timezone.now(),
                ended_at=None,
                created_by_user_id=user_fixture.id
            )

            user_story_input_dto = UserStoryInputDTO(
                id=None,
                name='User Story 1',
                display_id=1,
                content='Content of User Story 1',
                started_at=None,
                opened_merge_request_at=None,
                ended_at=None,
                created_by_user_id=user_fixture.id,
                epic_id=epic.id
            )
            return user_story_input_dto


        @pytest.mark.django_db
        def test_return_user_story_entity_when_creating_an_user_story(self, user_story_input_dto_fixture: UserStoryInputDTO):
            repository = UserStoryRepository()
            user_story = repository.save(user_story_input_dto_fixture)
            user = User.objects.get(name='user1')
            epic = Epic.objects.get(display_id=1)

            assert user_story.display_id == 1
            assert user_story.name == 'User Story 1'
            assert user_story.content == 'Content of User Story 1'
            assert user_story.started_at == None
            assert user_story.opened_merge_request_at == None
            assert user_story.ended_at == None
            assert user_story.created_by_user_id == user.id
            assert user_story.epic_id == epic.id