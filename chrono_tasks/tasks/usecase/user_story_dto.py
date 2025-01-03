from pydantic import BaseModel
from datetime import datetime

from tasks.domain.type import CreatedByUserId, EpicId

class UserStoryListInputDTO(BaseModel):
    """UserStory一覧取得に関する入力情報

    主にusecase層で利用されるが、presentation層でも利用される
    """
    offset: int
    limit: int

class UserStoryInputDTO(BaseModel):
    """UserStoryに関する入力情報

    主にusecase層で利用されるが、presentation層でも利用される
    """
    name: str
    display_id: int
    content: str
    started_at: datetime
    opened_merge_request_at: datetime
    ended_at: datetime

class UserStoryOutputDTO(BaseModel):
    """UserStoryに関する出力情報

    主にusecase層で利用されるが、presentation層でも利用される
    """
    id: int
    dipslay_id: int
    name: str
    content: str
    started_at: datetime
    opened_merge_request_at: datetime
    ended_at: datetime
    status: str
    created_by_user_id: CreatedByUserId
    epic_id: EpicId
    created_at: datetime
    updated_at: datetime