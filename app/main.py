from fastapi import FastAPI

import uvicorn


app = FastAPI()

from .schemas import TaskUpdate, TaskCreate

from database import crud

@app.put("/updateTask")
async def update(task: TaskUpdate):
    try:
        crud.update_task(task)
    except:
        return {"message": "bad request!"}
    return {"message": "Task updated!"}

@app.get("/getTask")
async def get_task(id: int):
    try:
        task = crud.get_task(id)
    except:
        return {"message": "bad request!"}
    return {"task": task}

@app.post("/createTask")
async def create_task(task: TaskCreate):
    try:
        crud.create_task(task)
    except:
        return {"message": "bad request!"}
    return {"message": "Task created!"}




if __name__ == "__main__":
    uvicorn.run(app)