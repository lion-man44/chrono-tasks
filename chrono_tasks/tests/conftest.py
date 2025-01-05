import pytest
from freezegun import freeze_time
from django.utils import timezone

from tasks.usecase.epic_dto import EpicInputDTO
from users.models import User

@pytest.fixture
@freeze_time('2021-01-01')
def user_fixture():
    return User.objects.create(
        name='user1',
        email='a@example.com'
    )

@pytest.fixture
@freeze_time('2021-01-01')
def epic_input_dto_fixture(_, user_input_dto_fixture):
    return EpicInputDTO(
        display_id = 1,
        name = 'Epic 1',
        content = 'Content of Epic 1',
        started_at = timezone.now(),
        opened_merge_request_at = timezone.now(),
        ended_at = timezone.now(),
        created_at = timezone.now(),
        updated_at = timezone.now(),
        created_by_user_id = user_input_dto_fixture.id
    )
