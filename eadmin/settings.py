import os
from pathlib import Path

from loguru import logger

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-5)pz4t$si&=b62_@9#58a2wmh@%lraeg(7j8dbdagm!94e2_$h"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    ###### Celery 配置 ######
    "django_celery_results",
    "django_celery_beat",
    ########################
    ##### API 文档配置 #####
    "drf_spectacular",
    "drf_spectacular_sidecar",
    #######################
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "eadmin.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "eadmin.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "zh-hans"

TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

USE_TZ = True


#################### 静态文件配置选项 ####################
# uwsgi staic-map 映射URL和文件夹路径
STATIC_URL = "eadmin/static/"
# python manage.py collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, "static")
########################################################

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


#################### LOGGING 配置选项 ####################
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"normal": {"format": "[%(asctime)s][%(levelname)s] %(message)s"}},
    "handlers": {
        "console": {
            "level": "DEBUG",
            "filters": None,
            "class": "logging.StreamHandler",
            "formatter": "normal",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
        },
    },
}
########################################################


#################### Celery 配置选项 ####################
# 删除指引：全局搜索关键字 "Celery 配置" 然后删除对应代码块
# 参考文档：https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html#using-celery-with-django
if os.environ.get("RUN_MAIN") != "true":
    logger.info("已集成 Celery")
CELERY_RESULT_BACKEND = "django-db"
CELERY_CACHE_BACKEND = "django-cache"
CELERY_BROKER_URL = "redis://10.12.196.158:6379/0"
########################################################


#################### API 文档配置选项 ####################
# 删除指引：全局搜索关键字 "API 文档" 然后删除对应代码块
# 参考文档：https://drf-spectacular.readthedocs.io/en/latest/readme.html#self-contained-ui-installation
if os.environ.get("RUN_MAIN") != "true":
    logger.info("已集成 API文档")
SPECTACULAR_SETTINGS = {
    "SWAGGER_UI_DIST": "SIDECAR",
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
    "SCHEMA_PATH_PREFIX": "/api/v1/eadmin/",
    "TITLE": "EADMIN DOCS",
}
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}
########################################################
