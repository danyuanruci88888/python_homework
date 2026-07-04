import logging
from fastapi import FastAPI
from models import Base
from database import engine
from routers.users import router as users_router
from routers.auth import router as auth_router
from routers.tasks import router as tasks_router
from routers.statistics import router as statistics_router
from routers.jobs import router as jobs_router
from routers.favorites import router as favorites_router
from routers.applications import router as applications_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI()

Base.metadata.create_all(bind=engine)
logger.info("数据库表已创建/同步完成")

app.include_router(users_router)
app.include_router(auth_router)
app.include_router(tasks_router)
app.include_router(statistics_router)
app.include_router(jobs_router)
app.include_router(favorites_router)
app.include_router(applications_router)
logger.info("所有路由已注册完成")