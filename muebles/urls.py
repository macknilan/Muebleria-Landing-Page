from django.conf.urls import url
from muebles.views import HomeView, ComedoresTemplateDetailView, CocinasTemplateDetailView, ClosetsTemplateDetailView, PuertasTemplateDetailView, BanosTemplateDetailView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^comedores/(?P<slug>[\w\-]+)/$', ComedoresTemplateDetailView.as_view(), name='detailcomedores'),
    url(r'^cocinas/(?P<slug>[\w\-]+)/$', CocinasTemplateDetailView.as_view(), name='detailcocinas'),
    url(r'^closets/(?P<slug>[\w\-]+)/$', ClosetsTemplateDetailView.as_view(), name='detailclosets'),
    url(r'^puertas/(?P<slug>[\w\-]+)/$', PuertasTemplateDetailView.as_view(), name='detailpuertas'),
    url(r'^banos/(?P<slug>[\w\-]+)/$', BanosTemplateDetailView.as_view(), name='detailbanos'),
]
