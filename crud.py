
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
    if all(v for v in data.values()):
        return data
    else:
        return {"status":"error", "message":"There are no tasks!"}


def task_by_id(task_id:str):
    # открываем json
    try:
        with open("db.json","r")as file:
            data = json.load(file)
    except FileNotFoundError:
        return {"status": "error", "message":"file not found!"}
        
    # находим элемента json по id
    for d in data["tasks"]:
        if d["id"] == task_id:
            return d
        
    return {"status":"error","message":"There is no task for this id"}


def task_by_name(task_name:str):
    try:
        with open("db.json","r")as file:
            data = json.load(file)
    except FileNotFoundError:
        return {"status": "error", "message":"file not found!"}
        
    list_d = []
    for d in data["tasks"]:
        if d["name"] == task_name:
            list_d.append(d)
        
    if len(list_d) > 0:
        return list_d
    return {"status":"error","message":"There is no task for this name"}


def task_by_name_sort(task_name:str,sort_asc:bool):
    list_d = task_by_name(task_name)
    
    if isinstance(list_d,dict):
        return list_d
    
    if len(list_d) <= 1:
        return list_d
    
    for i in range(0,len(list_d)):
        itm = list_d[i]["data_create"]
        index_itm = i
        for j in range(i+1,len(list_d)):
            time_j = list_d[j]["data_create"]
            
            if sort_asc: 
                if itm > time_j:
                    index_itm = j
            else:
                if itm < time_j:
                    index_itm = j
                
        if index_itm != i:
            list_d[i], list_d[index_itm] = list_d[index_itm], list_d[i]
    
    return list_d


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
    
    return {"status":"success", "message": "Task added!"} 


# ------------------- UPDATE -------------------

def update_task(task:Task, task_id:str):
    # открываем json
    try:
        with open("db.json","r") as file:
            data = json.load(file)
    except FileNotFoundError:
        return {"status": "error", "message":"file not found!"}
        
    # вносим изменения в json
    for i,d in enumerate(data["tasks"]):
        if d["id"] == task_id:
            # print(f"d = {d}")
            data["tasks"][i] = {
                "id": task_id,  
                "name": d["name"] if task.name.startswith("string") else task.name,
                "description": d["description"] if task.description.startswith("string") else task.description,
                "data_create": d["data_create"] if task.data_create.startswith("string") else task.data_create
            }
            
            # обновляем json
            with open("db.json","w") as file:
                json.dump(data,file, indent=4)
                
                
            return {"status":"success", "message":"Task updated!"}
    return {"status": "error", "message":"No such task was found in json!"}


# ------------------- DELETE -------------------

def delete_task(task_id:str):
    # открываем json
    try:
        with open("db.json","r") as file:
            data = json.load(file)
    except FileNotFoundError:
        return {"status": "error", "message":"file not found!"}
    
    # вносим изменения в json
    for d in data["tasks"]:
        if d["id"] == task_id:
            data["tasks"].remove(d)
            
    # обновляем json
    with open("db.json","w") as file:
        json.dump(data,file,indent=4)
        
        return {"status": "success", "message": "Task deleted!"}
    return {"status": "error", "message": "No such task was found in json!"}        
            

def delete_task_by_name(task_name:str):
    
    # открываем json
    try:
        with open("db.json","r") as file:
            data = json.load(file)
    except FileNotFoundError:
        return {"status": "error", "message":"file not found!"}
        
    original_count = len(data["tasks"])
    
    # Фильтруем задачи, которые не совпадают по имени
    data["tasks"] = [d for d in data["tasks"] if d["name"] != task_name]
    
    deleted_count = original_count - len(data["tasks"])

    if deleted_count > 0:
        # обновляем json
        with open("db.json", "w") as file:
            json.dump(data, file, indent=4)

        return {"status": "success", "message": f"{deleted_count} task(s) deleted!"}
    return {"status": "error", "message": "No such task was found in json!"}