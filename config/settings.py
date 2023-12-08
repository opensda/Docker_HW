import os
from datetime import timedelta
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django.contrib.postgres',
    "drf_yasg",
    "atomichabits",
    "users",
    "rest_framework",
    "corsheaders",
    "rest_framework_simplejwt",
    "django_celery_beat",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "config.urls"

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

WSGI_APPLICATION = "config.wsgi.application"



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Используется PostgreSQL
        'NAME': os.getenv("POSTGRES_DB"),  # Имя базы данных
        'USER': os.getenv("POSTGRES_USER"),  # Имя пользователя
        'PASSWORD': os.getenv("POSTGRES_PASSWORD"),  # Пароль пользователя
        'HOST': 'pgdb',  # Наименование контейнера для базы данных в Docker Compose
        'PORT': '5432',  # Порт базы данных
    }
}


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

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

AUTH_USER_MODEL = "users.User"

LOGOUT_REDIRECT_URL = "/"
LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "/users/"

STATIC_URL = "static/"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=150),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

# Настройка для доступа front-end
#CORS_ALLOWED_ORIGINS = [
#    "https://read-only.example.com",
#    "https://read-and-write.example.com",
#]

# Настройка для доступа back-end
#CSRF_TRUSTED_ORIGINS = [
#    "https://read-and-write.example.com",
#]

# URL-адрес брокера сообщений
CELERY_BROKER_URL = 'redis://redis:6379/0'

# URL-адрес брокера результатов, также Redis

CELERY_RESULT_BACKEND = 'redis://redis:6379/0'

# Часовой пояс для работы Celery
CELERY_TIMEZONE = "UTC"

# Флаг отслеживания выполнения задач
CELERY_TASK_TRACK_STARTED = True

# Максимальное время на выполнение задачи
CELERY_TASK_TIME_LIMIT = 30 * 60
