from typing import Optional

from sqlmodel import Field, SQLModel, create_engine

from datetime import datetime

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    completed: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


if __name__ == "__main__":
    engine = create_engine("sqlite:///database.db")
    SQLModel.metadata.create_all(engine)