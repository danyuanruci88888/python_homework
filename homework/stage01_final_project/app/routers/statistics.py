import logging
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import User, Task, Application, Tag
from routers.auth import get_current_user
from schemas import ProgressResponse
from services.redis_service import get_progress_cache, set_progress_cache

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/statistics", tags=["statistics"])


@router.get("/progress", response_model=ProgressResponse)
def get_progress(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user_id = current_user.id

  
    cached = get_progress_cache(user_id)
    if cached:
        logger.info(f"[Redis] 命中缓存: user:{user_id}:progress")
        return cached

    logger.info(f"[MySQL] 缓存未命中，查询数据库: user:{user_id}:progress")
    total = db.query(Task).filter(Task.user_id == user_id).count()
    completed = db.query(Task).filter(
        Task.user_id == user_id,
        Task.status == "已完成"
    ).count()
    completion_rate = round(completed / total * 100, 2) if total > 0 else 0.0
    application_count = db.query(Application).filter(
        Application.user_id == user_id
    ).count()

    tag_count = db.query(Tag).filter(
        Tag.user_id == user_id
    ).count()

    result = {
        "total": total,
        "completed": completed,
        "completion_rate": completion_rate,
        "application_count": application_count,
        "tag_count": tag_count
    }

    set_progress_cache(user_id, result, expire=60)
    logger.info(f"[Redis] 写入缓存: user:{user_id}:progress = {result}")

    return result
