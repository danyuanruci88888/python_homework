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
    application_count: int
    tag_count: int

class JobBase(BaseModel):
    title: str
    company: str
    location: str | None = None
    description: str | None = None

class JobCreate(JobBase):
    pass

class JobResponse(JobBase):
    id: int

    class Config:
        from_attributes = True

class FavoriteCreate(BaseModel):
    job_id: int

class FavoriteResponse(BaseModel):
    id: int
    user_id: int
    job_id: int

    class Config:
        from_attributes = True

class ApplicationCreate(BaseModel):
    job_id: int
    notes: str | None = None

class ApplicationUpdate(BaseModel):
    status: str
    notes: str | None = None

class ApplicationResponse(BaseModel):
    id: int
    user_id: int
    job_id: int
    status: str
    notes: str | None = None

    class Config:
        from_attributes = True

class TagCreate(BaseModel):
    name: str

class TagResponse(BaseModel):
    id: int
    name: str
    user_id: int

    class Config:
        from_attributes = True