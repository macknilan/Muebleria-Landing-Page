"""muebleria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('muebles.urls', namespace='muebles')),
    url(r'', include('categorias.urls', namespace='categorias')),
]

handler404 = 'categorias.views.not_found'
handler500 = 'categorias.views.server_error'
handler403 = 'categorias.views.permission_denied'
handler400 = 'categorias.views.bad_request'

if settings.DEBUG:
    """
    PARA SERVIR LOS ARCHIVOS ESTATICOS EN DESARROLLO
    """
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
