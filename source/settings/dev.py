from .base import *  # noqa: F403, F401

DEBUG = False

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
MIDDLEWARE.append("whitenoise.middleware.WhiteNoiseMiddleware")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# WAGTAILADMIN_BASE_URL required for notification emails
WAGTAILADMIN_BASE_URL = "http://localhost:8000"

ALLOWED_HOSTS = ["*"]

try:
    from .local import *  # noqa
except ImportError:
    pass
