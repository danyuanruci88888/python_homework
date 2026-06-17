import os
import json
import logging
import redis
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    db=0,
    decode_responses=True
)


def get_progress_cache(user_id: int):
    """从 Redis 获取用户学习进度缓存"""
    key = f"user:{user_id}:progress"
    data = redis_client.get(key)
    if data:
        logger.info(f"[Redis] 命中缓存: {key}")
        return json.loads(data)
    logger.info(f"[Redis] 缓存未命中: {key}")
    return None


def set_progress_cache(user_id: int, data: dict, expire: int = 60):
    """把用户学习进度写入 Redis，默认 60 秒过期"""
    key = f"user:{user_id}:progress"
    redis_client.set(key, json.dumps(data), ex=expire)
    logger.info(f"[Redis] 写入缓存: {key} = {data}")
