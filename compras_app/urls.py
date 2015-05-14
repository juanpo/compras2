__author__ = 'juan'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ProductosView.as_view(), name='productos'),
    url(r'^(?P<codigo>[A-Z0-9]+)/$', views.ProductosDetalleView.as_view(), name='detail'),
    url(r'^(?P<codigo>[A-Z0-9]+)/handle/$', views.handle, name='handle'),
    url(r'^(?P<codigo>[A-Z0-9]+)/borrar/$', views.ProductosBorrarView.as_view(), name='borrar'),
    url(r'^(?P<codigo>[A-Z0-9]+)/editar/$', views.ProductosEditarView.as_view(), name='editar'),
    url(r'^search$', views.ProductosSearchView.as_view(), name='search'),
    url(r'^crear/$', views.ProductosCrearView.as_view(), name='crear'),
    ]
