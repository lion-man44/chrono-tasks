from pydantic import BaseModel
from datetime import datetime
from typing import Union

from tasks.domain.type import CreatedByUserId, EpicId

class EpicListInputDTO(BaseModel):
    """Epic一覧取得に関する入力情報

    主にusecase層で利用されるが、presentation層でも利用される
    """
    offset: int
    limit: int

class EpicInputDTO(BaseModel):
    """Epicに関する入力情報

    主にusecase層で利用されるが、presentation層でも利用される
    """
    id: Union[EpicId, None]
    name: str
    display_id: int
    content: Union[str, None]
    started_at: Union[datetime, None]
    ended_at: Union[datetime, None]
    created_by_user_id: CreatedByUserId

class EpicOutputDTO(BaseModel):
    """Epicに関する出力情報

    主にusecase層で利用されるが、presentation層でも利用される
    """
    id: int
    dipslay_id: int
    name: str
    content: str
    started_at: datetime
    ended_at: datetime
    status: str
    created_by_user_id: CreatedByUserId
    created_at: datetime
    updated_at: datetime