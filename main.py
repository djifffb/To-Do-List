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


@app.get("/task_by_id/{task_id}")
def task_by_id(task_id:str):
    return crud.task_by_id(task_id)


@app.get("/task_by_name/{task_name}")
def task_by_name(task_name:str):
    return crud.task_by_name(task_name)


@app.get("/task_by_name/{task_name}/{sort_asc}")
def task_by_name_sort(task_name:str,sort_asc:bool):
    return crud.task_by_name_sort(task_name,sort_asc)


# -------------------- POST --------------------

@app.post("/tasks")
def create_task(task: Task):
    return crud.create_task(task)
    

# ------------------- UPDATE -------------------

@app.put("/tasks/{task_id}")
def update_task(task:Task, task_id:str):
    return crud.update_task(task, task_id)


# ------------------- DELETE -------------------

@app.delete("/delete_task_by_id/{task_id}")
def delete_task(task_id:str):
    return crud.delete_task(task_id)

@app.delete("/delete_tasks_by_name/{task_name}")
def delete_by_name(task_name:str):
    return crud.delete_task_by_name(task_name)
