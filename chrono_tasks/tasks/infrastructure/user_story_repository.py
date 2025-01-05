from tasks.domain.user_story_i_repository import UserStoryIRepository

from tasks.usecase.user_story_dto import UserStoryInputDTO
from tasks.domain.user_story_entity import UserStoryEntity
from tasks.models import UserStory
from tasks.usecase.user_story_dto import UserStoryListInputDTO

class UserStoryRepository(UserStoryIRepository):
    def save(self, user_story_input_dto: UserStoryInputDTO) -> UserStoryEntity:
        user_story = UserStoryEntity.from_dto(user_story_input_dto)
        UserStory.objects.update_or_create(
            id=user_story.id,
            defaults=user_story,
        )
        return UserStoryEntity.model_validate(user_story)

    def find_by_id(self, id: int) -> UserStoryEntity:
        pass

    def find_tasks_by_id(self, id: int):
        pass

    def list(self, user_story_list_input_dto: UserStoryListInputDTO) -> UserStoryEntity:
        pass

    def delete(self, user_story_input_dto: UserStoryInputDTO) -> UserStoryEntity:
        pass