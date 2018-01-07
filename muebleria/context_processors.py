# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.views.generic import ListView
from random import shuffle
from muebles.models import Mueble


def lista_link_muebles_relacionados(request):
    """
    LISTA DE MUEBLES RELACIONADOS COMO LINKS EN INFERIOR DE PAGINA
    """
    categoria_mueble_comedor = list(Mueble.objects.filter(categoria__cat_mueble="comedores")[:4])
    shuffle(categoria_mueble_comedor)
    categoria_mueble_cocina = list(Mueble.objects.filter(categoria__cat_mueble="cocinas")[:4])
    shuffle(categoria_mueble_cocina)
    categoria_mueble_closets = list(Mueble.objects.filter(categoria__cat_mueble="closets")[:4])
    shuffle(categoria_mueble_closets)
    categoria_mueble_puertas = list(Mueble.objects.filter(categoria__cat_mueble="puertas")[:4])
    shuffle(categoria_mueble_puertas)
    categoria_mueble_banos = list(Mueble.objects.filter(categoria__cat_mueble="banos")[:4])
    shuffle(categoria_mueble_banos)
    context = {
        'categoria_mueble_comedor': categoria_mueble_comedor,
        'categoria_mueble_cocina': categoria_mueble_cocina,
        'categoria_mueble_closets': categoria_mueble_closets,
        'categoria_mueble_puertas': categoria_mueble_puertas,
        'categoria_mueble_banos': categoria_mueble_banos,
    }
    return context

