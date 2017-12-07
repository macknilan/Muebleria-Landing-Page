from django.conf.urls import url
from categorias.views import ComedoresListView


urlpatterns = [
    url(r'^comedores/$', ComedoresListView.as_view(), name='comedores'),
]
