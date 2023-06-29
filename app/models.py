from pydantic import BaseModel

from datetime import datetime

from typing import Optional


class Task(BaseModel):
    id: Optional[int]
    title: str
    description: str
    completed: bool
    created_at: datetime = datetime.today()
    updated_at: datetime = datetime.today()

