
import json
import random
import string

from datetime import datetime
from model import Task
from typing import Optional


# -------------------- GET ---------------------

def all_task():
    with open("db.json","r") as file:
        data = json.load(file)
    return data


# -------------------- POST --------------------

def create_task(task:Task):
    chars = string.ascii_letters + string.digits  # Все буквы (a-zA-Z) + цифры (0-9)
    random_id = ''.join(random.choice(chars) for _ in range(5))
    new_task = {
        "id": random_id,
        "name": task.name,
        "description": task.description,
        "data_create": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    
    # открываем json
    try:
        with open("db.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"tasks": []}
    
    # вносим изменения в json
    data["tasks"].append(new_task)
    
    # обновляем json
    with open("db.json", "w") as file:
        json.dump(data,file,indent=4)
    


# ------------------- UPDATE -------------------

def update_task(task:Task, task_id:str):
    # открываем json
    try:
        with open("db.json","r") as file:
            data = json.load(file)
    except FileNotFoundError:
        return {"status": "error", "message":"file not found!"}
        
    for i,d in enumerate(data["tasks"]):
        if d["id"] == task_id:
            print(f"d = {d}")
            data["tasks"][i] = {
                "id": task_id,  
                "name": d["name"] if task.name.startswith("string") else task.name,
                "description": d["description"] if task.description.startswith("string") else task.description,
                "data_create": d["data_create"] if task.data_create.startswith("string") else  task.data_create
            }
            
            with open("db.json","w") as file:
                json.dump(data,file, indent=4)
                
            return {"status":"success", "message":"Task updated!"}
    return {"status": "error", "message":"Error 404"}


# ------------------- DELETE -------------------

    