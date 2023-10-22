import redis

from common.yaml_config import GetConf

class RedisOperation:
    def __init__(self):
        redis_info = GetConf().get_redis()
        self.redis_client = redis.Redis(
            host = redis_info["host"],
            port = redis_info["port"],
            db = redis_info["db"],
            decode_responses=True,
            charset="UTF-8",
            encoding = "UTF-8"
            # password=user:password
        )