### Celery 配置 ###
import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eadmin.settings")

app = Celery("eadmin")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


# ignore_result=True 可以让结果被忽略, 不写入数据库
# @app.task(bind=True, ignore_result=True)
@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
