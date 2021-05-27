import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'TEMP_KEY'
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS = [
    'upload',
]

MIDDLEWARE = [
]

ROOT_URLCONF = 'file_upload.urls'


WSGI_APPLICATION = 'file_upload.wsgi.application'


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

