from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import User, Task
from routers.auth import get_current_user
from schemas import ProgressResponse
from services.redis_service import get_progress_cache, set_progress_cache

router = APIRouter(prefix="/statistics", tags=["statistics"])


@router.get("/progress", response_model=ProgressResponse)
def get_progress(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user_id = current_user.id

    # 1. 先查 Redis 缓存
    cached = get_progress_cache(user_id)
    if cached:
        print(f"[Redis] 命中缓存: user:{user_id}:progress")
        return cached

    # 2. 缓存没有，查 MySQL
    print(f"[MySQL] 缓存未命中，查询数据库: user:{user_id}:progress")
    total = db.query(Task).filter(Task.user_id == user_id).count()
    completed = db.query(Task).filter(
        Task.user_id == user_id,
        Task.status == "已完成"
    ).count()
    completion_rate = round(completed / total * 100, 2) if total > 0 else 0.0

    result = {
        "total": total,
        "completed": completed,
        "completion_rate": completion_rate
    }

    # 3. 把结果写入 Redis，60 秒过期
    set_progress_cache(user_id, result, expire=60)
    print(f"[Redis] 写入缓存: user:{user_id}:progress = {result}")

    return result
