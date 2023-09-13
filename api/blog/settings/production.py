from .base import *

import os
import django_heroku
import dj_database_url

# CORS_ALLOWED_ORIGINS = [str('FRONTEND_URL')]

STATIC_ROOT = BASE_DIR / 'static'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

SECRET_KEY = str(os.environ.get('SECRET_KEY'))

ADMIN_URL = str(os.environ.get('ADMIN_URL'))

DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com']

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
DATABASES['default']['ATOMIC_REQUESTS'] = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

if 'HEROKU' in os.environ:
    django_heroku.settings(locals())