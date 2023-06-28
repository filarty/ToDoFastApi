from sqlmodel import select, create_engine, Session

from .sql_models import Task

from app.schemas import TaskCreate, TaskUpdate

from datetime import datetime

#connect to database
engine = create_engine("sqlite:///database.db")

def get_task(id: int) -> Task | None:
    #SELECT * FROM Task WHERE Task.id == id
    with Session(engine) as session:
        command = select(Task).where(Task.id == id)
        return session.exec(command).first()


def create_task(task: TaskCreate) -> None:
    #INSERT INTO Task VALUES (...)
    task_object = Task(id=task.id, title=task.title, description=task.description, created_at=task.created_at)
    with Session(engine) as session:
        session.add(task_object)
        session.commit()

def update_task(task: TaskUpdate) -> None:
    #UPDATE Task SET ... = ... WHERE Task.id == task.id
    with Session(engine) as session:
        command = select(Task).where(Task.id == task.id)
        result = session.exec(command).one()
        result.title = task.title
        result.description = task.description
        result.completed = task.complated
        result.updated_at = task.update_at
        session.add(result)
        session.commit()



if __name__ == "__main__":
    task = TaskUpdate(id=0, title="hello", description="change", complated=True, update_at=datetime.now())
    update_task(task)
    print(get_task(0))
    