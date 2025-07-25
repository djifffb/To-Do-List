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
    return {"message": "Task added"}
    




# ------------------- UPDATE -------------------
# ------------------- DELETE -------------------

    


