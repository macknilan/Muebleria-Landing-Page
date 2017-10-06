# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.urls import reverse
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.core.exceptions import ValidationError
from django.db import models


class SlugMixin(object):
    def get_slug(self, text, model):
        slug_text = slugify(text)
        # count = 2
        # fecha_ano = datetime.date.year()
        slug = slug_text
        if (model._default_manager.filter(slug=slug).exists()):
            raise ValidationError(_('ESTO ES UN MENSAJE DE PRUEBA - ERROR ESTO ESTA REPETIDO'))
        # while(model._default_manager.filter(slug=slug).exists()):
        #     slug = '{0}-{1}'.format(slug_text, count)
        return slug


def change_file_name(self, imagefilename):
    """
    FUNCION PARA CAMBIAR EL NOMBRE DE LA IMAGEN COMPONIENDOLO CON 
    EL SLUG_DIEZ_CARACTERES_RANDOM.EXTENCION Y GUARDAR IMAGEN EN CARPETA PERSONALIZADA
    """
    ext = imagefilename.split('.')[-1]
    imagefilename = "%s_%s.%s" % (self.slug, get_random_string(10), ext)

    return os.path.join('fotos_categoria', imagefilename)


@python_2_unicode_compatible
class Categoria(SlugMixin, models.Model):
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

    def get_absolute_url(self):
        return reverse('categorias:comedores', kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = self.get_slug(self.cat_mueble, Categoria)
        super(Categoria, self).save(*args, **kwargs)

    def __str__(self):
        return self.cat_mueble
