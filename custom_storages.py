# ARCHIVO PARA PODER SUBIR LOS ARCHIVOS ESTATICOS Y MEDIA
# DIGITAL OCEAN SPACES POR MEDIO DE ESTOS DOS PROGRAMAS django-storages & boto
# ESTO ECHO CON DJANGO


from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """
    ALMACENAMIENTO ARCHIVOS STATICOS
    """
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """
    ALMACENAMIENTO PARA ARCHIVOS MEDIA
    """
    location = settings.MEDIAFILES_LOCATION
