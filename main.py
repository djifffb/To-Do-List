from fastapi import FastAPI, HTTPException

# import
import crud 
from model import Task


app = FastAPI()

@app.get("/")
def default():
    return {"message":"this the home page"}

@app.post("/tasks")
def create_task(task: Task):
    success = crud.create_task(task)
    if not success:
        return HTTPException(status_code=400, detail="Task with this ID already exists")
    return {"message": "Task added"}
    
    


