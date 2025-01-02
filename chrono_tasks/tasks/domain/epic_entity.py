from typing import NewType
from uuid import UUID
from datetime import datetime

from pydantic import Field

from shared.domain.entity import BaseEntity
from shared.domain.value_object import EnumStatus
from type import EpicId, CreatedByUserId

class EpicEntity(BaseEntity):
    id: EpicId
    display_id: int = Field(ge=1)
    name: str
    content: str
    started_at: datetime
    opened_merge_request_at: datetime
    ended_at: datetime
    created_at: datetime
    updated_at: datetime
    created_by_user_id: CreatedByUserId

    def status(self) -> str:
        if self.started_at is None:
            return EnumStatus.TODO.value
        if self.ended_at is None:
            return EnumStatus.IN_PROGRESS.value
        return EnumStatus.DONE.value