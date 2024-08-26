# EADMIN

## Celery 集成

### 安装

```bash
pip install -U "celery[redis]" django-celery-results django-celery-beat
```

在 *setting.py* 文件新增：

```py
INSTALLED_APPS = [
    ...
    ###### Celery 配置 ######
    "django_celery_results",
    "django_celery_beat",
    ########################
]

#################### Celery 配置选项 ####################
# 删除指引：全局搜索关键字 "Celery 配置" 然后删除对应代码块
# 参考文档：https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html#using-celery-with-django
if os.environ.get("RUN_MAIN") != "true":
    logger.info("已集成 Celery")
CELERY_RESULT_BACKEND = "django-db"
CELERY_CACHE_BACKEND = "django-cache"
CELERY_BROKER_URL = "redis://10.12.196.158:6379/0"
########################################################
```

和 *setting.py* 同级目录，新建文件 *celery.py*

```py
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


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
```

和 *setting.py* 同级目录，新建文件 `__init__.py`

```py
# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ("celery_app",)
```

最后执行迁移

```bash
python manage.py migrate
```

### 运行

```bash
# 启动 celery worker
celery -A eadmin worker -l INFO
# 启动 celery beat
celery -A eadmin beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

## API 文档集成

### 安装

```bash
pip install drf-spectacular[sidecar]
```

在 *setting.py* 文件新增：

```py
INSTALLED_APPS = [
    ...
    ##### API 文档配置 #####
    "drf_spectacular",
    "drf_spectacular_sidecar",
    #######################
]

SPECTACULAR_SETTINGS = {
    'SWAGGER_UI_DIST': 'SIDECAR',  # shorthand to use the sidecar instead
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
    # OTHER SETTINGS
}
```