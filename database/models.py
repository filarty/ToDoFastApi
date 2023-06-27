from typing import Optional

from sqlmodel import Field, SQLModel, Session, create_engine, select

from datetime import datetime

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    completed: Optional[bool] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

task = Task(id=0, title="hello", description="dawda", completed=False, created_at=datetime.now())

engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    statements = select(Task).where(Task.id == 0)
    print(session.exec(statements).first())