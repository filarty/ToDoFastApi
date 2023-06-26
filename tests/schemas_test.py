from schemas import TaskBase, TaskCreate, TaskUpdate

from datetime import datetime


def test_task_base():
    task = TaskBase(title="hello", description="hello")
    assert task.title == "hello"
    assert task.description == "hello"
    

def test_task_create():
    task = TaskCreate(title="first", description="hello", created_at=datetime.now())
    assert task.title == "first"
    assert task.description == "hello"
    assert isinstance(task.created_at, datetime)


def test_task_update():
    task = TaskUpdate(title="update", description="hello", update_at=datetime.now(), complated=False)
    assert task.title == "update"
    assert task.description == "hello"
    assert isinstance(task.update_at, datetime)
    assert task.complated == False