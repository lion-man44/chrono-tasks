from datetime import datetime

from pydantic import Field

from shared.domain.entity import BaseEntity
from shared.domain.value_object import EnumStatus
from type import UserStoryId, TaskId, CreatedByUserId

class TaskEntity(BaseEntity):
    id: TaskId
    display_id: int = Field(ge=1)
    name: str
    content: str
    started_at: datetime
    opened_merge_request_at: datetime
    ended_at: datetime
    created_at: datetime
    updated_at: datetime
    created_by_user_id: CreatedByUserId
    user_story_id: UserStoryId

    def status(self) -> str:
        if self.started_at is None:
            return EnumStatus.TODO.value
        if self.opened_merge_request_at is None:
            return EnumStatus.IN_PROGRESS.value
        if self.ended_at is None:
            return EnumStatus.REVIEW.value
        return EnumStatus.DONE.value