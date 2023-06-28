from typing import Optional

from sqlmodel import Field, SQLModel

from datetime import datetime

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    completed: Optional[bool] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

