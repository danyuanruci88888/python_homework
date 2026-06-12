from fastapi import FastAPI
from models import Base
from database import engine
from routers.users import router as users_router
from routers.auth import router as auth_router
from routers.tasks import router as tasks_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users_router)
app.include_router(auth_router)
app.include_router(tasks_router)
