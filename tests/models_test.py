from models import Task



def test_model_Task():
    task = Task(id=1, title="first", description="hello, world!", completed=False)
    
    assert task.id == 1
    assert task.title == "first"
    assert task.description == "hello, world!"
    assert task.completed == False