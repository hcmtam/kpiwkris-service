from abc import ABCMeta
from upstash_redis import Redis
import os


class RedisManager(object):

    __metaclass__ = ABCMeta

    def __init__(self):

        self.redis = Redis(
            url=os.environ["UPSTASH_REDIS_REST_URL"],
            token=os.environ["UPSTASH_REDIS_REST_TOKEN"],
        )

    def exist_cache(self, key):
        return self.redis.exists(key)

    def get_cache(self, key):

        exist = self.exist_cache(key)
        if not exist:
            return None

        value = self.redis.get(key)
        return value

    def set_cache(self, key, value):
        res = self.redis.set(key, value)
        return res

    def cache_attempt(self, key, value):
        res = self.set_cache(key, value)
        return res

    def get_last_attempt(self, session):
        res = self.redis.get(session)
        return res
