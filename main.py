from fastapi import FastAPI

import uvicorn


app = FastAPI()

from schemas import TaskUpdate


@app.put("/updateTask")
async def update(id: int, task: TaskUpdate):
    return {"model": task}



if __name__ == "__main__":
    uvicorn.run(app)