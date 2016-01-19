"""
Django settings for booklist project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import dj_database_url
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

in_heroku = "IT_IS_HEROKU" in os.environ
# heroku config:add MY_VAR='my_value'

if not in_heroku:
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'd9s1@(w6b98&!$0&3i-)5j9()j6_x%270)m3v_s6(_&bwua)5%'
else:
    SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'list',
    'widget_tweaks',
    'haystack',
    'elasticsearch',
    'floppyforms',
    'djcelery',
    'kombu.transport.django',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'booklist.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'booklist.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

if not in_heroku:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        "default": dj_database_url.config()
    }

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Novosibirsk'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': "list.search_backends.CustomElasticSearchEngine",
        'URL': 'http://booksearch-djachenko.rhcloud.com:80/',
        'INDEX_NAME': 'haystack',
        'TIMEOUT': 60
    }
}

if not in_heroku:
    BROKER_URL = 'django://'
    CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'
else:
    BROKER_URL = os.environ['REDIS_URL']
    CELERY_RESULT_BACKEND = os.environ['REDIS_URL']
