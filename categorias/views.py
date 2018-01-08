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


class CocinasListView(ListView):
    """
    CLASE PARA DESPLEGAR LOS COCINAS EN LISTA
    """
    model = Mueble
    template_name = "CocinasCategoryTemplateView.html"
    paginate_by = 1
    ordering = ["id"]

    def get_queryset(self):
        queryset = super(CocinasListView, self).get_queryset()
        return queryset.filter(categoria__cat_mueble="cocinas")


class ClosetsListView(ListView):
    """
    CLASE PARA DESPLEGAR LOS CLOSETS EN LISTA
    """
    model = Mueble
    template_name = "ClosetsCategoryTemplateView.html"
    paginate_by = 1
    ordering = ["id"]

    def get_queryset(self):
        queryset = super(ClosetsListView, self).get_queryset()
        return queryset.filter(categoria__cat_mueble="closets")


class PuertasListView(ListView):
    """
    CLASE PARA DESPLEGAR LOS PUERTAS EN LISTA
    """
    model = Mueble
    template_name = "PuertasCategoryTemplateView.html"
    paginate_by = 1
    ordering = ["id"]

    def get_queryset(self):
        queryset = super(PuertasListView, self).get_queryset()
        return queryset.filter(categoria__cat_mueble="puertas")


class BanosListView(ListView):
    """
    CLASE PARA DESPLEGAR LOS BAÑOS EN LISTA
    """
    model = Mueble
    template_name = "BanosCategoryTemplateView.html"
    paginate_by = 1
    ordering = ["id"]

    def get_queryset(self):
        queryset = super(BanosListView, self).get_queryset()
        return queryset.filter(categoria__cat_mueble="banos")
