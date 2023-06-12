from models import Task

from datetime import date

from pydantic import validator



class TaskCreate(Task):
    title: str
    description: str
    created_at: date
    
    @validator("title")
    def not_empty(cls, title):
        if not title.strip():
            raise ValueError("Title cannot by empty")
        return title

    
    
class TaskUpdate(Task):
    completed: bool
    description: str
    updated_at: str
    
    @validator("completed")
    def true_or_false(cls, completed):
        if type(completed) is not bool:
            raise ValueError("Completed flag must bool")