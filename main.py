from fastapi import FastAPI

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


@app.get("/task_id/{task_id}")
def task_by_id(task_id:str):
    return crud.task_by_id(task_id)


@app.get("/task_name/{task_name}")
def task_by_name(task_name:str):
    return crud.task_by_name(task_name)




# -------------------- POST --------------------

@app.post("/tasks")
def create_task(task: Task):
    return crud.create_task(task)
    

# ------------------- UPDATE -------------------

@app.put("/tasks/{task_id}")
def update_task(task:Task, task_id:str):
    return crud.update_task(task, task_id)


# ------------------- DELETE -------------------

@app.delete("/tasks/{task_id}")
def delete_task(task_id:str):
    return crud.delete_task(task_id)


