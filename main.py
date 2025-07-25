from fastapi import FastAPI, HTTPException

# import
import crud 
from model import Task


app = FastAPI()

@app.get("/")
def default():
    return {"message":"this the home page"}

@app.post("/tasks")
def create_task(description: Task):
    success = crud.create_task(description)
    if not success:
        return HTTPException(status_code=400, detail="Task with this ID already exists")
    return {"message": "Task added"}
    
    


