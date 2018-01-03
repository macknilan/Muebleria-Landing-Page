from django.conf.urls import url
from muebles.views import HomeView, ComedoresTemplateDetailView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^comedores/(?P<slug>[\w\-]+)/$', ComedoresTemplateDetailView.as_view(), name='detailcomedores'),
]
