from sqlmodel import select, SQLModel, create_engine, Session, insert

from sql_models import Task

from main.schemas import TaskCreate

from datetime import datetime

engine = create_engine("sqlite:///database.db")


def get_task(id: int) -> Task | None:
    with Session(engine) as session:
        command = select(Task).where(Task.id == id)
        return session.exec(command).first()


def create_task(task: TaskCreate) -> None:
    with Session(engine) as session:
        session.add(task)
        session.commit()

task = TaskCreate(id=0, title="hello", description="first", created_at=datetime.now())

if __name__ == "__main__":
    create_task(task)
    print(get_task(0))