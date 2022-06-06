"""
Django settings for projectcocktails project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import datetime
from pathlib import Path
import os
import dj_database_url
import environ
import cloudinary
import cloudinary.uploader
import cloudinary.api

env = environ.FileAwareEnv()

environ.FileAwareEnv.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'apps.cocktails.apps.CocktailsConfig',
    'apps.ingredients.apps.IngredientsConfig',
    'apps.cauth.apps.AuthConfig',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'projectcocktails.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'projectcocktails.wsgi.application'

CSRF_COOKIE_SECURE = False
CSRF_TRUSTED_ORIGINS = ['https://projectcocktails.herokuapp.com']
# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASE_URL = 'postgresql://<postgresql>'
DATABASES = {'default': dj_database_url.config('DATABASE_URL')}

# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': env('DB_NAME'),
#         'CLIENT': {
#                 'host': 'localhost',
#                 'port': 27017,
#                 'authSource': 'project_db',
#             },
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL = 'media/'
MEDIA_ROOT = 'media/'

CRISPY_TEMPLATE_PACK = "bootstrap4"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"


cloudinary.config(
    cloud_name=env('CLOUDINARY_NAME'),
    api_key=env('CLOUDINARY_APIKEY'),
    api_secret=env('CLOUDINARY_APISECRET')
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'base_format': {
            'format': '{asctime} - {levelname}: {message}',
            'style': '{',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'base_format',
        },
        'info': {
            'class': 'logging.FileHandler',
            'formatter': 'base_format',
            'filename': 'info-logs.log',
        },
        'error': {
            'class': 'logging.FileHandler',
            'formatter': 'base_format',
            'filename': 'error-logs.log',
        },
    },
    'loggers': {
        'root': {
            'handlers': ['info', 'error', 'console'],
            'level': 1,
        },
    },
}