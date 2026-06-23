"""
Django settings for tutor_connect_project project.

These settings are suitable for local development and testing.
For production, you should use environment variables
"""

from pathlib import Path

import dj_database_url
from decouple import config

# ---------------------------------------------------------------------
# Base paths
# ---------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent


# ---------------------------------------------------------------------
# Security
# ---------------------------------------------------------------------

# Keep the production secret key in an environment variable.
SECRET_KEY = config('SECRET_KEY')

# DEBUG should be False in production.
DEBUG = config("DEBUG", default=False, cast=bool)

# Add your deployed domain here when moving beyond Heroku defaults.
ALLOWED_HOSTS = ["localhost", "127.0.0.1", ".herokuapp.com"]


# ---------------------------------------------------------------------
# Applications
# ---------------------------------------------------------------------

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

PROJECT_APPS = [
    "accounts",
    "tutors",
    "bookings",
    "checkout",
    "django_filters",
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS

# ---------------------------------------------------------------------
# Middleware
# ---------------------------------------------------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # Serves compressed static files efficiently in production.
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ---------------------------------------------------------------------
# URLs and templates
# ---------------------------------------------------------------------

ROOT_URLCONF = 'tutor_connect_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tutor_connect_project.wsgi.application'

# ---------------------------------------------------------------------
# Database
# ---------------------------------------------------------------------

database_url = config("DATABASE_URL", default="")

if database_url:
    DATABASES = {
        "default": dj_database_url.parse(database_url, conn_max_age=600)
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
# ---------------------------------------------------------------------
# Password validation
# ---------------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': (
            'django.contrib.auth.password_validation'
            '.UserAttributeSimilarityValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation'
            '.MinimumLengthValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation'
            '.CommonPasswordValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation'
            '.NumericPasswordValidator'
        ),
    },
]

# ---------------------------------------------------------------------
# Stripe
# ---------------------------------------------------------------------

STRIPE_PUBLIC_KEY = config("STRIPE_PUBLIC_KEY", default="")
STRIPE_SECRET_KEY = config("STRIPE_SECRET_KEY", default="")
STRIPE_WEBHOOK_SECRET = config("STRIPE_WEBHOOK_SECRET", default="")

# ---------------------------------------------------------------------
# Internationalization
# ---------------------------------------------------------------------

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# ---------------------------------------------------------------------
# Static files
# ---------------------------------------------------------------------

STATIC_URL = "/static/"

# Local static files used during development.
STATICFILES_DIRS = [BASE_DIR / "static"]

# Destination for collected static files in production.
STATIC_ROOT = BASE_DIR / "staticfiles"

# Enables WhiteNoise to serve compressed, cache-friendly static assets.
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ---------------------------------------------------------------------
# Media files
# ---------------------------------------------------------------------

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ---------------------------------------------------------------------
# Authentication redirects
# ---------------------------------------------------------------------

LOGIN_REDIRECT_URL = "dashboard"
LOGOUT_REDIRECT_URL = "home"
LOGIN_URL = "login"
