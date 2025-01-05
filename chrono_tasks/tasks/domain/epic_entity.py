from uuid import uuid4
from datetime import datetime

from typing import Union
from pydantic import Field

from shared.domain.entity import BaseEntity
from shared.domain.value_object import EnumStatus
from tasks.domain.type import EpicId, CreatedByUserId

class EpicEntity(BaseEntity):
    id: EpicId = uuid4
    display_id: int = Field(ge=1)
    name: str = ''
    content: Union[str, None] = None
    started_at: Union[datetime, None] = None
    opened_merge_request_at: Union[datetime, None] = None
    ended_at: Union[datetime, None] = None
    created_by_user_id: Union[CreatedByUserId, None] = None

    def status(self) -> str:
        if self.started_at is None:
            return EnumStatus.TODO.value
        if self.ended_at is None:
            return EnumStatus.IN_PROGRESS.value
        return EnumStatus.DONE.value