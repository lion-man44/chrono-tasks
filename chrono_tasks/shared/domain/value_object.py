from pydantic import BaseModel
from enum import Enum

class BaseValueObject(BaseModel):
    class Config:
        frozen = True

class EnumStatus(Enum):
    TODO = 'To-do'
    IN_PROGRESS = 'In-progress'
    REVIEW = 'Review'
    DONE = 'Done'