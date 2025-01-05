from datetime import datetime
from typing import Union
from pydantic import Field
from uuid import uuid4

from shared.domain.entity import BaseEntity
from shared.domain.value_object import EnumStatus
from tasks.domain.type import EpicId, UserStoryId, CreatedByUserId
from tasks.usecase.user_story_dto import UserStoryInputDTO

class UserStoryEntity(BaseEntity):
    id: UserStoryId = uuid4()
    display_id: int = Field(ge=1)
    name: str = ''
    content: Union[str, None] = None
    started_at: Union[datetime, None] = None
    opened_merge_request_at: Union[datetime, None] = None
    ended_at: Union[datetime, None] = None
    created_by_user_id: Union[CreatedByUserId, None] = None
    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None
    epic_id: EpicId

    @classmethod
    def from_dto(cls, dto: UserStoryInputDTO):
        return cls(
            display_id=dto.display_id,
            name=dto.name,
            content=dto.content,
            started_at=dto.started_at,
            opened_merge_request_at=dto.opened_merge_request_at,
            ended_at=dto.ended_at,
            created_by_user_id=dto.created_by_user_id,
            epic_id=dto.epic_id
        )

    def status(self) -> str:
        if self.started_at is None:
            return EnumStatus.TODO.value
        if self.opened_merge_request_at is None:
            return EnumStatus.IN_PROGRESS.value
        if self.ended_at is None:
            return EnumStatus.REVIEW.value
        return EnumStatus.DONE.value