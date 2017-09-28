# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Categoria


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('cat_mueble', 'slug', )
    list_filter = ('cat_mueble', 'slug', )
    search_fields = ['cat_mueble', ]
    readonly_fields = ('slug', )
