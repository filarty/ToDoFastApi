from schemas import TaskBase, TaskCreate, TaskUpdate

from datetime import datetime

def test_task_base():
    #create test for TaskBase object
    task = TaskBase(id=0, title="hello", description="hello")
    assert task.title == "hello"
    assert task.description == "hello"
    assert task.id == 0

def test_task_create():
    #create test for TaskCreate object
    task = TaskCreate(id=0, title="first", description="hello", created_at=datetime.now())
    assert task.title == "first"
    assert task.description == "hello"
    assert isinstance(task.created_at, datetime)
    assert task.id == 0

def test_task_update():
    #create test for TaskUpdate object
    task = TaskUpdate(id=0, title="update", description="hello", update_at=datetime.now(), complated=False)
    assert task.id == 0
    assert task.title == "update"
    assert task.description == "hello"
    assert isinstance(task.update_at, datetime)
    assert task.complated == False
    
def test_task_title_not_empty():
    #check value for title in object Task
    try:
        task = TaskBase(id=0, title="", description="hello")
    except ValueError:
        assert True
    
    try:
        task = TaskBase(id=0, title=" ", description="hello")
    except ValueError:
        assert True
    