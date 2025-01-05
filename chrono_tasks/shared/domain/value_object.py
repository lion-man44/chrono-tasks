from pydantic import BaseModel, ConfigDict
from enum import Enum

class BaseValueObject(BaseModel):
    model_config = ConfigDict(strict=True, frozen=True)

class EnumStatus(Enum):
    TODO = 'To-do'
    IN_PROGRESS = 'In-progress'
    REVIEW = 'Review'
    DONE = 'Done'