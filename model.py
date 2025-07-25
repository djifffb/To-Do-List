from pydantic import BaseModel

class Task(BaseModel):
    id: str
    name: str
    description: str
    data_create: str
    