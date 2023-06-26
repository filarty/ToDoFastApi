from pydantic import BaseConfig
from datetime import date



class Task(BaseConfig):
    id: int
    title: str
    description: str
    completed: bool
    created_at: date = date.today()
    updated_at: date = date.today()

