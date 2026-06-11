from pydantic import BaseModel

class UserCreate(BaseModel):
    username:str
    password:str

class UserResponse(BaseModel):
    username:str
    password:str

class UserResponse(BaseModel):
    id:int
    username:str

    class Config:
        from_attributes = True
        
class UserLogin(BaseModel):
    username:str
    password:str

class UserLogin(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class TaskResponse(BaseModel):
    id:int
    title:str
    status:str
    user_id:int

    class Config:
        from_attributes = True
        
