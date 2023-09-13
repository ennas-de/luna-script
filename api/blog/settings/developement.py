from .base import *

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
]

BASE_URL = 'http://127.0.0.1:8000'

MEDIA_URL = '/media-url/'

MEDIA_ROOT = BASE_DIR / 'media'

SECRET_KEY = 'secret_key'

ADMIN_URL = 'admin/'

DEBUG = True

ALLOWED_HOSTS = ['*']