# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from categorias.models import Categoria


class HomeView(TemplateView):
    """
    CLASE PARA MOSTRAR LAS FOTOGRAFIAS EN LA PAGINA INICIAL
    """
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['pictures_fpss'] = Categoria.objects.all()
        return context












