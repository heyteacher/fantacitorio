"""
Django settings for fc_project project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import json

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# caricamento il locale delle variabili di ambiente di sviluppo se non già valorizzate
if os.environ.get('STAGE') is None and os.environ.get('DATABASE_DEFAULT_HOST') is None:
    json_data = open('zappa_settings.json')
    env_vars = json.load(json_data)['local']['environment_variables']
    for key, val in env_vars.items():
        os.environ[key] = val

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = "true" == os.environ.get('DEBUG', '').lower() 

ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS_1'),os.environ.get('ALLOWED_HOSTS_2'),]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
     # moduli aggiuntivi
    'django_s3_storage',
    'django_s3_sqlite',
    'django_dynamodb_cache',
    'django_filters',
    'admin_auto_filters',
    'import_export',
    'django_tables2',
    'django_bootstrap5',
     'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.twitter_oauth2',
    # le due applicazioni
    'fc_gestione_app',
    'fc_classifiche_app'
]

SITE_ID = 1
#ACCOUNT_EMAIL_VERIFICATION = "none"
#LOGIN_REDIRECT_URL = "home"
#ACCOUNT_LOGOUT_ON_GET = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fc_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'fc_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_DEFAULT_ENGINE'),
        'NAME': os.environ.get('DATABASE_DEFAULT_NAME'),

        'USER': os.environ.get('DATABASE_DEFAULT_USER'),
        'PASSWORD': os.environ.get('DATABASE_DEFAULT_PASSWORD'),
        'HOST': os.environ.get('DATABASE_DEFAULT_HOST'),
        'PORT': os.environ.get('DATABASE_DEFAULT_PORT'),
        # django_s3_sqlite 
        'BUCKET': os.environ.get('DATABASE_DEFAULT_BUCKET'),
    }
}

if not os.environ.get('DATABASE_CLASSIFICHE_ENGINE') == '':
    DATABASES['db_classifiche'] = {
            'ENGINE': os.environ.get('DATABASE_CLASSIFICHE_ENGINE'),
            'NAME': os.environ.get('DATABASE_CLASSIFICHE_NAME'),
            # django_s3_sqlite 
            'BUCKET': os.environ.get('DATABASE_CLASSIFICHE_BUCKET'),
    }

DATABASE_ROUTERS = [
    'fc_gestione_app.routers.GestioneRouter', 
    'fc_classifiche_app.routers.ClassificheRouter'
]

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'it-IT'

TIME_ZONE = 'Europe/Rome'

USE_I18N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# DJANGO S3 STATIC
if not os.environ.get('STATICFILES_STORAGE','') == '':
    STATICFILES_STORAGE = os.environ.get('STATICFILES_STORAGE')
    AWS_S3_BUCKET_NAME_STATIC = os.environ.get('AWS_S3_BUCKET_NAME_STATIC')
    AWS_S3_KEY_PREFIX_STATIC = os.environ.get('AWS_S3_KEY_PREFIX_STATIC')

    # These next two lines will serve the static files directly 
    # from the s3 bucket
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_S3_BUCKET_NAME_STATIC
    STATIC_URL = "https://%s/%s" % (AWS_S3_CUSTOM_DOMAIN, AWS_S3_KEY_PREFIX_STATIC)

    # OR...if you create a fancy custom domain for your static files use:
    if not os.environ.get('AWS_CLOUDFRONT_ENDPOINT','') == '':
        AWS_S3_PUBLIC_URL_STATIC = "%s/%s" % (os.environ.get('AWS_CLOUDFRONT_ENDPOINT') ,AWS_S3_KEY_PREFIX_STATIC)
else:
    STATIC_URL = 'static/'
    STATIC_ROOT = 'static/'

# Django Cache + Session Engine
if not os.environ.get('CACHE_DEFAULT_BACHEND','') == '':
    CACHES = {
        "default": {
            "BACKEND": os.environ.get('CACHE_DEFAULT_BACHEND'), 
            "LOCATION": os.environ.get('CACHE_DEFAULT_LOCATION'), 
            "OPTIONS": {
                "aws_region_name": os.environ.get('CACHE_DEFAULT_AWS_REGION') 
            }
        }
    }
    SESSION_ENGINE = "django.contrib.sessions.backends.cache"

# SMTP Settings
if not os.environ.get('EMAIL_HOST','') == '':
    EMAIL_HOST = os.environ.get('EMAIL_HOST')
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
    EMAIL_PORT= os.environ.get('EMAIL_PORT')
    DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
    EMAIL_SUBJECT_PREFIX = os.environ.get('EMAIL_SUBJECT_PREFIX')
    EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', '').lower() == 'true'
    EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL', '').lower() == 'true'

# Django Table2 settings
DJANGO_TABLES2_PAGE_RANGE=5

# Bootstrap5 settings
BOOTSTRAP5 = {
    'server_side_validation': False
}

if DEBUG:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
            },
        },
        'root': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }