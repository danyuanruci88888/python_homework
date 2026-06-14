import redis
import json

redis_client = redis.Redis(
    host='localhost',
    port=6379,
    db=0,
    decode_responses=True
)

def get_progress_cache(user_id:int):
    """从 Redis 获取用户学习进度缓存"""
    key = f"user:{user_id}:progress"
    data = redis_client.get(key)
    if data :
        return json.loads(data)
    return None

def set_progress_cache(user_id:int ,data:dict,expire:int = 60):
    """把用户学习进度写入 Redis ,默认 60 秒过期"""
    key = f"user:{user_id}:progress"
    redis_client.set(key,json.dumps(data),ex=expire)