from pydantic import BaseModel,Field
from typing import Literal

class TaskCreate(BaseModel):
    title:str = Field(...,min_length=1,max_length=50)
    status:Literal["todo","doing","done"] = "todo"
    difficulty : int = Field(default=1,ge = 1,le = 5)

class TaskUpdate(BaseModel):
    title:str |None = Field(default = None , min_length = 1,max_length = 50)
    status: Literal["todo","doing","done"]|None = None
    difficulty:int|None = Field(default = None ,ge = 1,le = 5)
