from .settings import *

DEBUG = False

ALLOWED_HOSTS = ['155.138.213.155']

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)