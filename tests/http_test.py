import requests

from datetime import datetime

def test_get_task():
    "Check return for getTask API method"
    id = 0
    response = requests.get("http://127.0.0.1:8000/getTask", params={"id": id})
    assert response.json() == {"message": "Ok!"}
    assert response.status_code == 200


def test_create_task():
    "Check create task in createTask API method"
    payload = {"id": "0", "title": "hello, world!", "description": "first", "created_at": str(datetime.now())}
    response = requests.post("http://127.0.0.1:8000/createTask", json=payload)
    assert response.json() == {"message": "Task created!"}
    assert response.status_code == 200

def test_update_task():
    "Check update for updateTask API method"
    payload = {"id": "0", "title": "hello, world!", "description": "first", "update_at": str(datetime.now()), "complated": True}
    response = requests.put("http://127.0.0.1:8000/updateTask", json=payload)
    assert response.json() == {"message": "Task updated!"}
    assert response.status_code == 200