# -*- coding: utf-8 -*-
"""
Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

from __future__ import unicode_literals

import os

from django.urls import reverse_lazy
from django.utils.crypto import get_random_string


def generate_secret_key(filename):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    with open(filename, "w") as file:
        file.write("SECRET_KEY='{0}'".format(get_random_string(50, chars)))


def get_bool_var(var: str, default: bool) -> bool:
    return os.getenv(var, str(default)).lower() == 'true'


def get_env(var: str, default):
    from_env = os.getenv(var)

    if from_env == 'None':
        return None

    return os.getenv(var, default)


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
try:
    from .secret_key import SECRET_KEY
except ImportError:
    settings_dir = os.path.abspath(os.path.dirname(__file__))
    generate_secret_key(os.path.join(PROJECT_DIR, 'settings', 'secret_key/__init__.py'))
    from .secret_key import SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_bool_var('DEBUG', False)

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'django.contrib.humanize',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'sekizai',
    'sorl.thumbnail',
    'django_nyt',
    'wiki',
    'wiki.plugins.macros',
    'wiki.plugins.help',
    'wiki.plugins.links',
    'wiki.plugins.images',
    'wiki.plugins.attachments',
    'wiki.plugins.notifications',
    'wiki.plugins.globalhistory',
    'mptt',
]

TEST_RUNNER = 'django.test.runner.DiscoverRunner'


MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

ROOT_URLCONF = 'wikiproject.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.request",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "sekizai.context_processors.sekizai",
            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'wikiproject.wsgi.application'
LOGIN_REDIRECT_URL = reverse_lazy('wiki:get', kwargs={'path': ''})


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.' + os.getenv('DB_TYPE', 'sqlite3'),
        'NAME': os.path.join(PROJECT_DIR, 'db', os.getenv('DB_NAME', 'db.sqlite3')),
        'USER': get_env('DB_USER', None),
        'PASSWORD': get_env('DB_PASSWORD', None),
        'HOST': get_env('DB_HOST', None),
        'PORT': get_env('DB_PORT', None),
        'CHARSET': get_env('DB_CHARSET', None),
        'COLLATION': get_env('DB_COLLATION', None),
        'DATAFILE': get_env('DB_ORA_DATAFILE', None),
        'DATAFILE_TMP': get_env('DB_ORA_DATAFILE_TMP', None),
        'DATAFILE_MAXSIZE': get_env('DB_ORA_DATAFILE_MAXSIZE', None),
        'DATAFILE_TMP_MAXSIZE': get_env('DB_ORA_DATAFILE_TMP_MAXSIZE', None),
        'DATAFILE_SIZE': get_env('DB_ORA_DATAFILE_SIZE', None)
    }
}

if get_bool_var('USE_CACHE', False):
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.' + get_env('CACHE_TYPE', 'filebased.FileBasedCache'),
            'LOCATION': get_env('CACHE_LOCATION', '/var/tmp/django_cache'),
            'KEY_PREFIX': get_env('CACHE_KEY_PREFIX', ''),
            'TIMEOUT': int(get_env('CACHE_TIMEOUT', 300))
        }
    }


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

TIME_ZONE = os.getenv('TZ', 'Europe/Warsaw')

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = os.getenv('LANGUAGE_CODE', 'en-US')

SITE_ID = int(os.getenv('SITE_ID', 1))
USE_I18N = True
USE_L10N = True
USE_TZ = get_bool_var('USE_TZ', True)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
MEDIA_URL = '/media/'

WIKI_ANONYMOUS_WRITE = get_bool_var('WIKI_ANONYMOUS_WRITE', True)
WIKI_ANONYMOUS_CREATE = get_bool_var('WIKI_ANONYMOUS_CREATE', False)
