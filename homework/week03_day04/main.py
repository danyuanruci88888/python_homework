from fastapi import FastAPI

from routers.users import router as users_router
from models import Base
from database import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users_router)