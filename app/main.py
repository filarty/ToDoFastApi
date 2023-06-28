from fastapi import FastAPI

import uvicorn


app = FastAPI()

from schemas import TaskUpdate, TaskCreate

from models import Task


@app.put("/updateTask")
async def update(task: TaskUpdate):
    return {"message": "Task updated!"}

@app.get("/getTask")
async def get_task(id: int):
    return {"message": "Ok!"}

@app.post("/createTask")
async def create_task(task: TaskCreate):
    return {"message": "Task created!"}




if __name__ == "__main__":
    uvicorn.run(app)