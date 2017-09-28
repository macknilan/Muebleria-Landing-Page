# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Categoria(models.Model):
    CAT_M = (
        ('ninguno', 'Ninguno'),
        ('comedores', 'Comedores'),
        ('cocinas', 'Cocinas'),
        ('closets', 'Closets'),
        ('banos', 'Banos'),
    )
    cat_mueble = models.CharField("Categoria del Mueble", max_length=10, choices=CAT_M, default='ninguno')
    imagen_categoria = models.ImageField("Foto de Categoria", upload_to='cat_imgs/', max_length=50)
    slug = models.CharField(max_length=140, blank=True, unique=True)

    def __str__(self):
        return self.cat_mueble
