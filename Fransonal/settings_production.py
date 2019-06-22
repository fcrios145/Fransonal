from .settings import *

DEBUG = False

ALLOWED_HOSTS = ['mztprogramming.com', 'www.mztprogramming.com']
# ALLOWED_HOSTS = ['206.189.216.180',]


# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)