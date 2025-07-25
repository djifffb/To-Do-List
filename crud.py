
import json
import random
import string

from datetime import datetime
from model import Task


def create_task(task:Task):

    chars = string.ascii_letters + string.digits  # Все буквы (a-zA-Z) + цифры (0-9)
    random_id = ''.join(random.choice(chars) for _ in range(5))
    new_task = {
        "id": random_id,
        "name": task.name,
        "description": task.description,
        "data_create": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    
    try:
        with open("db.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"tasks": []}
    
    data["tasks"].append(new_task)
    
    with open("db.json", "w") as file:
        json.dump(data,file,indent=4)
        
    return True
    

