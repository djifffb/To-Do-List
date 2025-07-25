from fastapi import FastAPI, HTTPException

# import
import crud 
from model import Task


app = FastAPI()

# -------------------- GET ---------------------


@app.get("/")
def default():
    return {"message":"this the home page"}


@app.get("/tasks")
def all_task():
    return crud.all_task()






# -------------------- POST --------------------

@app.post("/tasks")
def create_task(task: Task):
    crud.create_task(task)
    return {"message": "Task added!"}
    


# ------------------- UPDATE -------------------

@app.put("/tasks/{task_id}")
def update_task(task:Task, task_id:str):
    return crud.update_task(task, task_id)

# ------------------- DELETE -------------------

    


