from pydantic import BaseModel

class BaseEntity(BaseModel):
    class Config:
        validate_assignment = True
