import time

import redis
from redis.lock import Lock

from eadmin.celery import app

redis_client = redis.StrictRedis(host="10.12.196.158", port=6379)
lock = Lock(redis_client, "lock", timeout=10)


# ignore_result=True 可以让结果被忽略, 不写入数据库
# @app.task(bind=True, ignore_result=True)
@app.task(bind=True)
def debug_task(self):
    with lock:
        time.sleep(10)
        print(f"Request: {self.request!r}")
