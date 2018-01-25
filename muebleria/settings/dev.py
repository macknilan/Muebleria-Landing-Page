#
from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['MUEBLERIALLAVE']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

INSTALLED_APPS += (
    'django_extensions',

)

"""   [STATIC & MEDIA FILES]   """

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


"""
SE ANADE LA RUTA PARA STATIC Y MEDIA FILES AFUERA DE CARPETA DE PROYECTO EN CARPETA COLLECT_STATIC
"""
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "COLLECT_STATIC", "static_root")
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "COLLECT_STATIC", "media_root")

"""   [STATIC & MEDIA FILES]   """
































