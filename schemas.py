from pydantic import BaseModel
from datetime import datetime


class TaskBase(BaseModel):
    title: str
    description: str



class TaskCreate(TaskBase):
    created_at: datetime


class TaskUpdate(TaskBase):
    complated: bool
    update_at: datetime