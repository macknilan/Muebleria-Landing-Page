# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Mueble


@admin.register(Mueble)
class MuebleAdmin(admin.ModelAdmin):
    list_display = ('slug', 'modelo', 'descripcion', 'dimensiones', 'categoria', 'oferta', 'precio', 'foto_1', 'foto_2', 'foto_3', 'foto_4', 'foto_5', )
    list_filter = ('modelo', 'categoria', )
    search_fields = ['descripcion', 'modelo', ]
    readonly_fields = ('slug', )
    list_editable = ('modelo', 'descripcion', 'dimensiones', 'categoria', 'oferta', 'precio', )
    # prepopulated_fields = {"slug": ("modelo",)}
