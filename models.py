from pydantic import BaseConfig

class Task(BaseConfig):
    id: int
    title: str
    description: str
    completed: bool
    created_at: str
    updated_at: str

