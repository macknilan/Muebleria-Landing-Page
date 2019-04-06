# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, FormView, TemplateView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from muebles.models import Mueble
from .forms import ContactForm


def server_error(request):
    """
    FUNCION PARA PERSONALIZAR LA PAGINA DE ERROR 500
    """
    return render(request, '500.html')


def not_found(request):
    """
    FUNCION PARA PERSONALIZAR LA PAGINA DE ERROR 404
    """
    return render(request, '404.html')


def permission_denied(request):
    """
    FUNCION PARA PERSONALIZAR LA PAGINA DE ERROR 403
    """
    return render(request, '403.html')


def bad_request(request):
    """
    FUNCION PARA PERSONALIZAR LA PAGINA DE ERROR 400
    """
    return render(request, '400.html')


class ComedoresListView(ListView):
    """
    CLASE PARA DESPLEGAR LOS COMEDORES EN LISTA
    """
    model = Mueble
    template_name = "ComedoresCategoryTemplateView.html"
    paginate_by = 4
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
    paginate_by = 4
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
    paginate_by = 4
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
    paginate_by = 4
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
    paginate_by = 4
    ordering = ["id"]

    def get_queryset(self):
        queryset = super(BanosListView, self).get_queryset()
        return queryset.filter(categoria__cat_mueble="banos")


class PreguntasYRespuestasTemplate(TemplateView):
    """
    CLASE PARA MOSTRAR TEMPLATE DE PREGUNTAS Y RESPUESTAS
    """
    template_name = "Pyr.html"


class ContactFormView(FormView):
    """
    CLASE PARA EL FORMULARIO DE CONTACTO, MANDA MAIL POR MEDIO DE GMAIL,
    NO SE OCUPA UN MODELO PARA GUARDARLO EN BD
    """
    template_name = 'ContactTemplateView.html'
    form_class = ContactForm
    success_url = reverse_lazy('muebles:home')

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        sender = form.cleaned_data['sender']
        message = form.cleaned_data['message']

        body = (
            "Nombre/Titulo: %s \n" % subject
            + "Envia: %s \n" % sender
            + "Mensaje: %s \n" % message
        )

        mail = EmailMessage(subject, body, sender, ['mail@gmail.com'], reply_to=['noreply@gmail.com'])
        # CHANGE -mail@gmail.com- FOR EMAIL TO WORK
        # import ipdb; ipdb.set_trace() # ESTO ES PARA DEBUGEAR
        mail.send()

        return super(ContactFormView, self).form_valid(form)
