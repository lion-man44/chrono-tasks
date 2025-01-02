from typing import NewType
from uuid import UUID

EpicId = NewType('EpicId', UUID)
UserStoryId = NewType('UserStoryId', UUID)
TaskId = NewType('TaskId', UUID)
CreatedByUserId = NewType('CreatedByUserId', UUID)
