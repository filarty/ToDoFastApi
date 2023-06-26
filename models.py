from pydantic import BaseModel
from datetime import datetime



class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool
    created_at: datetime = datetime.today()
    updated_at: datetime = datetime.today()

