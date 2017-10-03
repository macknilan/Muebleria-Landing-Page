# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.utils.crypto import get_random_string
from django.db import models




def change_file_name(self, imagefilename):
    """
    FUNCION PARA CAMBIAR EL NOMBRE DE LA IMAGEN COMPONIENDOLO CON 
    EL SLUG_DIEZ_CARACTERES_RANDOM.EXTENCION Y GUARDAR IMAGEN EN CARPETA PERSONALIZADA
    """
    ext = imagefilename.split('.')[-1]
    imagefilename = "%s_%s.%s" % (self.slug, get_random_string(10), ext)

    return os.path.join('fotos_categoria', imagefilename)


class Categoria(models.Model):
    CAT_M = (
        ('ninguno', 'Ninguno'),
        ('comedores', 'Comedores'),
        ('cocinas', 'Cocinas'),
        ('closets', 'Closets'),
        ('banos', 'Banos'),
    )
    cat_mueble = models.CharField("Categoria del Mueble", max_length=10, choices=CAT_M, default='ninguno')
    imagen_categoria = models.ImageField("Foto de Categoria", upload_to=change_file_name, max_length=50)
    slug = models.CharField(max_length=140, blank=True, unique=True)

    def __str__(self):
        return self.cat_mueble
