import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wq%Cr|2NKJ4wijqyJ7LnIQriso9xvCwu1RM3Z~IAPAiy8AnzQX'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'barkol',
        'USER': 'barkol',
        'PASSWORD': '08108108',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
}

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)