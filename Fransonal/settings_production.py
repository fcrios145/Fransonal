from .settings import *

DEBUG = False

# ALLOWED_HOSTS = ['mztprogramming.com', 'www.mztprogramming.com']
ALLOWED_HOSTS = ['167.99.162.3',]


# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)