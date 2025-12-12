"""
Django settings for instalalarm project.
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-change-this-in-production'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
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

ROOT_URLCONF = 'instalalarm.urls'

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

WSGI_APPLICATION = 'instalalarm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'pl-pl'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email configuration
# ============================================
# KONFIGURACJA EMAILI
# ============================================
# EMAIL_HOST_USER - Email Przemysława Stolarza (nadawca wiadomości)
#                   To jest email, z którego będą wysyłane wiadomości
#                   Przykład: 'przemyslaw.stolarz@gmail.com' lub 'ps.instalalarm@gmail.com'
#
# EMAIL_HOST_PASSWORD - Hasło do konta email powyżej
#                       Dla Gmail: użyj HASŁA APLIKACJI (nie zwykłego hasła!)
#                       Jak utworzyć hasło aplikacji Gmail:
#                       1. Wejdź na: https://myaccount.google.com/apppasswords
#                       2. Wybierz "Aplikacja" i "Poczta"
#                       3. Wybierz "Urządzenie" (np. Komputer)
#                       4. Kliknij "Generuj" i skopiuj wygenerowane hasło (16 znaków)
#
# CONTACT_EMAIL - Email, na który będą przychodzić wiadomości z formularza
#                 To też email Przemysława Stolarza (może być ten sam co EMAIL_HOST_USER)
#                 Przykład: 'przemyslaw.stolarz@gmail.com' lub 'ps.instalalarm@gmail.com'
#
# Dla Gmaila:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ps.instalalarm@gmail.com'  # Wpisz tutaj swój email Gmail (np. 'przemyslaw.stolarz@gmail.com')
EMAIL_HOST_PASSWORD = ''  # Wpisz tutaj HASŁO APLIKACJI Gmail (16 znaków, nie zwykłe hasło!)
DEFAULT_FROM_EMAIL = 'InstalAlarm <{}>'.format(EMAIL_HOST_USER) if EMAIL_HOST_USER else 'InstalAlarm'
CONTACT_EMAIL = 'ps.instalalarm@gmail.com'  # Wpisz tutaj email, na który mają przychodzić wiadomości (może być ten sam co EMAIL_HOST_USER)

# Dla innych serwerów email (np. własna domena):
# EMAIL_HOST = 'smtp.twoja-domena.pl'  # Zmień na swój serwer SMTP
# EMAIL_PORT = 587  # lub 465 dla SSL
# EMAIL_USE_TLS = True  # lub EMAIL_USE_SSL = True dla portu 465
# EMAIL_HOST_USER = 'ps.instalalarm@gmail.com'
# EMAIL_HOST_PASSWORD = 'twoje-haslo'
# DEFAULT_FROM_EMAIL = 'InstalAlarm <ps.instalalarm@gmail.com>'
# CONTACT_EMAIL = 'ps.instalalarm@gmail.com'

# Cache configuration (dla rate limiting)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
