import os
from dotenv import load_dotenv
from pathlib import Path
import sentry_sdk
import logging
from sentry_sdk.integrations.logging import LoggingIntegration

load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent


sentry_logging = LoggingIntegration(level=logging.INFO, event_level=logging.ERROR)


sentry_sdk.init(
    dsn="https://cc78634eb4a3e90b6f8d929c81a06827@o4508847959113728.ingest.de.sentry.io/4508883017334864",
    integrations=[sentry_logging],
    send_default_pii=True,
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)
logging.basicConfig(level=logging.INFO)


SECRET_KEY = os.getenv('SECRET_KEY')


DEBUG = False
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'python-oc-lettings-fr-on58.onrender.com']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lettings.apps.LettingsConfig',
    'profiles.apps.ProfilesConfig',
    'oc_lettings_site',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'oc_lettings_site.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'oc_lettings_site', 'templates'),
            os.path.join(BASE_DIR, 'profiles', 'templates'),
            os.path.join(BASE_DIR, 'lettings', 'templates'),
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


WSGI_APPLICATION = 'oc_lettings_site.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'oc-lettings-site.sqlite3'),
    }
}


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


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static",]

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
