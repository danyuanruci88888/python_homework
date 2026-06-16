from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TaskCreate(BaseModel):
    title: str
    status: str

class TaskResponse(BaseModel):
    id: int
    title: str
    status: str
    user_id: int

    class Config:
        from_attributes = True


class ProgressResponse(BaseModel):
    total: int
    completed: int
    completion_rate: float
