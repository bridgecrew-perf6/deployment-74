"""
Django settings for CNX_Protect project.
Generated by 'django-admin startproject' using Django 3.2.4.
For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os.path
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# from import auth

import webpage.apps

# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4y#ro1fpk^_w8wy9f@-a=k9#&6@d&1@m#an(9-vd4#y6&)xe0y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# https://protectcnx.azurewebsites.net

# ALLOWED_HOSTS = ['protectcnx.azurewebsites.net','djangowithdocker.azurewebsites.net','localhost']
# CSRF_TRUSTED_ORIGINS = ['https://protectcnx.azurewebsites.net','https://djangowithdocker.azurewebsites.net','http://localhost:8081/']
# ALLOWED_HOSTS = []
ALLOWED_HOSTS = 'cnxdeployment.azurewebsites.net'
# ['cnxdeployment.azurewebsites.net']

CSRF_TRUSTED_ORIGINS = ['https://cnxdeployment.azurewebsites.net', 'https://djangowithdocker.azurewebsites.net',
#                         'http://localhost:8081/']
# Application definition
INSTALLED_APPS = [
    'CNXProtect_Utl.apps.CnxprotectUtlConfig',
    'webpage.apps.WebpageConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap_datepicker_plus',
    'import_export',
    'account',
    'ContractLby',
    'whitenoise.runserver_nostatic'

    # 'admin_view_permission',
]
# ADMIN_VIEW_PERMISSION_MODELS = [
#     auth.User,
#     ...
# ]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CNX_Protect.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates\CNXProtect_Utl')],
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

WSGI_APPLICATION = 'CNX_Protect.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# DATABASES['default'] = dj_database_url.config()
# DATABASES['default']['ENGINE'] = 'django_postgrespool'
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'CNXProtect_Utl',
#         'USER': 'postgres',
#         'PASSWORD': '1234',
#         'HOST': 'localhost'
#     }
# }
DATABASES = {

'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'cnx_protect',
    'USER': 'Cipdev@devcip',
    'PASSWORD': 'Cnxcip@12345',
    'HOST': 'devcip.postgres.database.azure.com',
    'PORT': '5432',
    "OPTIONS": {"sslmode": "require"},
}

    # 'default': {

    #     # 'ENGINE': 'django.db.backends.postgresql',
    #     # # 'SERVER': 'devcip.postgres.database.azure.com',
    #     # 'PORT': '5432',
    #     # 'NAME': 'cnx_protect',
    #     # # 'DBNAME': 'POSTGRES',
    #     # 'USER': 'Cipdev@devcip',
    #     # 'PASSWORD': 'Cnxcip@12345',
    #     # 'HOST': 'devcip.postgres.database.azure.com',
    #     # 'OPTIONS': {'SslMode': 'Require'},

    #     # 'ENGINE': 'django.db.backends.postgresql',
    #     # # 'SERVER': 'devcip.postgres.database.azure.com',
    #     # 'PORT': '5432',
    #     # 'NAME': 'django',
    #     # # 'DBNAME': 'POSTGRES',
    #     # 'USER': 'Cipdev@devcip',
    #     # 'PASSWORD': 'Cnxcip@12345',
    #     # 'HOST': 'devcip.postgres.database.azure.com',
    #     # # 'OPTIONS': {'SslMode': 'Require'},


    #     # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     # 'ENGINE': 'django.db.backends.postgresql',
    #     # # 'NAME': 'CNXProtect_Utl',
    #     # 'NAME': 'cnx_protect',
    #     # # 'USER': 'postgres',
    #     # 'USER': 'Cipdev',
    #     # 'PASSWORD': '12345',
    #     # 'HOST': 'devcip.postgres.database.azure.com'
    #     # 'host' = 'devcip.postgres.database.azure.com',
    #     #  'port' = '5432',
    #     #  'username' =''<admin-user>'',
    #     #  'dbname' = 'postgres'

    #     # 'ENGINE': 'django.db.backends.postgresql',
    #     # 'NAME': 'CNXProtect_Utl',
    #     # 'USER': 'Cipdev@devcip',
    #     # 'PASSWORD': '1234',
    #     # 'HOST': 'localhost'

    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'CNXProtect_Utl',
    #     'USER': 'postgres',
    #     'PASSWORD': '1234',
    #     'HOST': 'localhost'
    # }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = '/static/'

# STATIC_URL = os.environ.get('DJANGO_STATIC_URL', '/static/')
MEDIA_URL = "/media/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'CNXProtect_Utl/static')
]

# STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
STATIC_ROOT = os.environ.get('DJANGO_STATIC_ROOT', 'assets')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFileStorage'
