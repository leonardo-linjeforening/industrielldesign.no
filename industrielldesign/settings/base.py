"""
Django settings for industrielldesign project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from . import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'otmxj!sqb^b8$sdv@o-2&iiatwa0@bb6)rz$$1j6#hamw&jfn_'

ALLOWED_HOSTS = ['LeonardoLinjeforening.pythonanywhere.com', 'www.industrielldesign.no', 'localhost', 'industrielldesign.herokuapp.com']

AUTH_USER_MODEL = 'authentication.Profile'

# EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = "mail.uniweb.no"
EMAIL_USE_SSL = True
EMAIL_HOST_USER = "ikkesvar@industrielldesign.no"
EMAIL_HOST_PASSWORD = config.EMAIL_PASSWORD
EMAIL_PORT = 465
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # My apps:
    'home',
    'wiki',
    'events',
    'projects',
    'authentication',
    'designsystem',
    'emails',
    'profilepage',
    'courses',
    'job',
    # Third party apps:
    'imagekit'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'industrielldesign.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates',
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'..', 'db.sqlite3'),
    }
}

WSGI_APPLICATION = 'industrielldesign.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'nb'

USE_TZ = True

TIME_ZONE = 'Europe/Oslo'

USE_I18N = True

USE_L10N = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static_in_pro')

# Django registration redux settings:

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
