# -*- coding: utf-8 -*-
from __future__ import unicode_literals


import os
from django.urls import reverse
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from categorias.models import Categoria


class SlugMixin(object):
    def get_slug(self, text, model):
        slug_text = slugify(text)
        # count = 2
        # fecha_ano = datetime.date.year()

        slug = slug_text
        # while(model._default_manager.filter(slug=slug).exists()):
        #    slug = '{0}-{1}'.format(slug_text, count)
        return slug


def change_file_name(self, imagefilename):
    """
    FUNCION PARA CAMBIAR EL NOMBRE DE LA IMAGEN COMPONIENDOLO CON EL SLUG_DIEZ_CARACTERES_RANDOM.EXTENCION
    """
    ext = imagefilename.split('.')[-1]
    imagefilename = "%s_%s.%s" % (self.slug, get_random_string(10), ext)

    return os.path.join('fotos', imagefilename)


@python_2_unicode_compatible
class Mueble(SlugMixin, models.Model):
    descripcion = models.TextField("Descripcion del mueble", max_length=240)
    dimensiones = models.TextField("Dimenciones del mueble", max_length=240)
    foto_1 = models.ImageField("1ra foto del mueble", upload_to=change_file_name, max_length=50)
    foto_2 = models.ImageField("2da foto del mueble", upload_to=change_file_name, max_length=50)
    foto_3 = models.ImageField("3ra foto del mueble", upload_to=change_file_name, max_length=50)
    foto_4 = models.ImageField("4ta foto del mueble", upload_to=change_file_name, max_length=50)
    foto_5 = models.ImageField("5ta foto del mueble", upload_to=change_file_name, max_length=50)
    modelo = models.CharField("Modelo (Nombre) ", max_length=40)
    oferta = models.SmallIntegerField("¿Oferta?", default=0)
    """
    CERO = NO TIENE OFERTA, DIFERENTE DE CERO SI TIENE OFERTA
    """
    precio = models.DecimalField("Precio del mueble", max_digits=10, decimal_places=2)
    slug = models.CharField(max_length=140, unique=True, blank=True)
    categoria = models.ForeignKey(Categoria)

    def get_absolute_url(self):
        return reverse('muebles:detailcomedores', kwargs={'slug': self.slug})
        # return '/%s/%s/' % (self.categoria, self.slug)

    def save(self, *args, **kwargs):
        self.slug = self.get_slug(self.modelo, Mueble)
        super(Mueble, self).save(*args, **kwargs)

    def __str__(self):
        return "%s - %s" % (self.modelo, self.descripcion)
