# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.views.generic.list import ListView
from django.shortcuts import render
from muebles.models import Mueble


class ComedoresListView(ListView):
    """
    CLASE PARA DESPLEGAR LOS COMEDORES EN LISTA
    """
    model = Mueble
    template_name = "ComedoresCategoryTemplateView.html"
    paginate_by = 1
    ordering = ["id"]

    def get_queryset(self):
        queryset = super(ComedoresListView, self).get_queryset()
        return queryset.filter(categoria__cat_mueble="comedores")
