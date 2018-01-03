# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from categorias.models import Categoria
from .models import Mueble


class HomeView(TemplateView):
    """
    CLASE PARA MOSTRAR LAS FOTOGRAFIAS EN LA PAGINA INICIAL
    """
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['pictures_fpss'] = Categoria.objects.all()
        return context


class ComedoresTemplateDetailView(DetailView):
    """
    CLASE PARA MOSTRAR LOS COMEDORES EN FORMA DE DETALLE/INDIVIDUAL
    """
    model = Mueble
    template_name = "MuebleTemplateDetailView.html"

    def get_queryset(self):
        if self.kwargs.get('slug'):
            queryset = self.model.objects.filter(slug=self.kwargs['slug'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ComedoresTemplateDetailView, self).get_context_data(**kwargs)
        context['categoria'] = 'comedores'
        return context









