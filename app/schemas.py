from pydantic import BaseModel, validator

from datetime import datetime

from typing import Optional

import re


class TaskBase(BaseModel):
    id: Optional[int]
    title: str
    description: str

    @validator('title')
    def check_not_empty(cls, value):
        if re.findall(r'[a-zA-Z]', value) == []:
            raise ValueError("title musst not empty!")
        return value

class TaskCreate(TaskBase):
    created_at: datetime


class TaskUpdate(TaskBase):
    complated: bool
    update_at: datetime