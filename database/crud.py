from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from sqlalchemy.ext.asyncio import create_async_engine


from .sql_models import Task

from app.schemas import TaskCreate, TaskUpdate

from datetime import datetime

#connect to database
engine = create_async_engine("sqlite+aiosqlite:///database.db", echo=True)



async def get_task(id: int) -> Task | None:
    #SELECT * FROM Task WHERE Task.id == id
    async with AsyncSession(engine) as session:
        command = select(Task).where(Task.id == id)
        result = await session.exec(command)
        return result.scalar()

async def create_task(task: TaskCreate) -> None:
    #INSERT INTO Task VALUES (...)
    task_object = Task(id=task.id, title=task.title, description=task.description, created_at=task.created_at)
    async with AsyncSession(engine) as session:
        session.add(task_object)
        await session.commit()

async def update_task(task: TaskUpdate) -> None:
    #UPDATE Task SET ... = ... WHERE Task.id == task.id
    async with AsyncSession(engine) as session:
        command = select(Task).where(Task.id == task.id)
        result = await session.exec(command).one()
        result.title = task.title
        result.description = task.description
        result.completed = task.complated
        result.updated_at = task.update_at
        session.add(result)
        await session.commit()



if __name__ == "__main__":
    task = TaskUpdate(id=0, title="hello", description="change", complated=True, update_at=datetime.now())
    ...
    