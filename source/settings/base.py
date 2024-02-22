import os
import dj_database_url

env_vars = os.environ.copy()

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

if 'DJANGO_SECRET_KEY' in env_vars:
    SECRET_KEY = env_vars["DJANGO_SECRET_KEY"]

if "DJANGO_ALLOWED_HOSTS" in env_vars:
    ALLOWED_HOSTS = env_vars["DJANGO_ALLOWED_HOSTS"].split(",")

INSTALLED_APPS = [
    "pricing",
    "features",
    "services",
    "base",
    "blog",
    "wagtail.api.v2",
    "wagtail.locales",
    "wagtail.contrib.routable_page",
    "wagtail.contrib.table_block",
    "wagtail.contrib.search_promotions",
    "wagtail.contrib.settings",
    "wagtail.contrib.simple_translation",
    "wagtail.contrib.styleguide",
    "rest_framework",
    "wagtailfontawesomesvg",
    "debug_toolbar",
    "django_extensions",
    "django.contrib.sitemaps",
    "home",
    "search",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

ROOT_URLCONF = "source.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "wagtail.contrib.settings.context_processors.settings",
            ],
        },
    },
]

WSGI_APPLICATION = "source.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": env_vars["MYSQL_DATABASE"] if "MYSQL_DATABASE" in env_vars else "",
        "USER": env_vars["MYSQL_USER"] if "MYSQL_USER" in env_vars else "",
        "PASSWORD": env_vars["MYSQL_PASSWORD"] if "MYSQL_PASSWORD" in env_vars else "",
        "HOST": env_vars["MYSQL_HOST"] if "MYSQL_HOST" in env_vars else "",
        "PORT": env_vars["MYSQL_PORT"] if "MYSQL_PORT" in env_vars else "",
    }
}

# if "DATABASE_URL" in os.environ:
#     DATABASES = {"default": dj_database_url.config(conn_max_age=500)}
# else:
#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.sqlite3",
#             "NAME": os.path.join(BASE_DIR, "bakerydemodb"),
#         }
#     }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
]

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# JavaScript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/4.2/ref/contrib/staticfiles/#manifeststaticfilesstorage
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"


# Wagtail settings

# WAGTAIL_SITE_NAME = "source"
WAGTAIL_SITE_NAME = env_vars["WAGTAIL_SITE_NAME"] if "WAGTAIL_SITE_NAME" in env_vars else ""


# Search
# https://docs.wagtail.org/en/stable/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {
    "default": {"BACKEND": "wagtail.search.backends.database", "INDEX": "striker"}
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
# WAGTAILADMIN_BASE_URL = "http://striker.pythonanywhere.com"
WAGTAILADMIN_BASE_URL = env_vars["BASE_URL"] if "BASE_URL" in env_vars else ""

WAGTAIL_I18N_ENABLED = True

WAGTAIL_CONTENT_LANGUAGES = LANGUAGES = [
    ("en", "English"),
    ("de", "Deutsch"),
    ("ar", "العربيّة"),
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Email Configuration
EMAIL_HOST = "smtp.gmail.com"
# EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_HOST_USER = "templatevoyage@gmail.com"
EMAIL_HOST_PASSWORD = "zgap njcr zdzg lnzi"
EMAIL_PORT = "587"
EMAIL_USE_TLS = True
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"  # new


INTERNAL_IPS = [
    '127.0.0.1',
]
