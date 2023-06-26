from pydantic import BaseModel, validator
from datetime import datetime


class TaskBase(BaseModel):
    id: int
    title: str
    description: str

    @validator('title')
    def check_not_empty(cls, value):
        if value == " " or value == "":
            raise ValueError("title musst not empty!")
        return value

class TaskCreate(TaskBase):
    created_at: datetime


class TaskUpdate(TaskBase):
    complated: bool
    update_at: datetime