from pydantic import BaseConfig
from datetime import datetime



class Task(BaseConfig):
    id: int
    title: str
    description: str
    completed: bool
    created_at: datetime = datetime.today()
    updated_at: datetime = datetime.today()

