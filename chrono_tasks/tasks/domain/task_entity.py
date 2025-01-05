from datetime import datetime

from typing import Union
from pydantic import Field

from shared.domain.entity import BaseEntity
from shared.domain.value_object import EnumStatus
from tasks.domain.type import UserStoryId, TaskId, CreatedByUserId

class TaskEntity(BaseEntity):
    id: TaskId
    display_id: int = Field(ge=1)
    name: str = ''
    content: Union[str, None] = None
    started_at: Union[datetime, None] = None
    opened_merge_request_at: Union[datetime, None] = None
    ended_at: Union[datetime, None] = None
    created_by_user_id: Union[CreatedByUserId, None] = None
    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None
    user_story_id: UserStoryId

    def status(self) -> str:
        if self.started_at is None:
            return EnumStatus.TODO.value
        if self.opened_merge_request_at is None:
            return EnumStatus.IN_PROGRESS.value
        if self.ended_at is None:
            return EnumStatus.REVIEW.value
        return EnumStatus.DONE.value