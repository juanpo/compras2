__author__ = 'juan'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ProductosView.as_view(), name='productos'),
    url(r'^(?P<codigo>[A-Z0-9]+)/$', views.detail, name='detail'),
    url(r'^descripcion_asc/$', views.DescripcionAscView.as_view(), name='descripcion_asc'),
    url(r'^descripcion_desc/$', views.DescripcionDescView.as_view(), name='descripcion_desc'),
    url(r'^codigo_asc/$', views.ProductosView.as_view(), name='index'),
    url(r'^codigo_desc/$', views.CodigoDescView.as_view(), name='descripcion_desc'),
]
