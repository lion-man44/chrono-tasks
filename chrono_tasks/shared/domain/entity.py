from pydantic import BaseModel, ConfigDict

class BaseEntity(BaseModel):
    model_config = ConfigDict(strict=True, validate_assignment=True)
