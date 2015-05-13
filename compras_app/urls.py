__author__ = 'juan'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ProductosView.as_view(), name='productos'),
    url(r'^(?P<codigo>[A-Z0-9]+)/$', views.DetalleProducto.as_view(), name='detail'),
    url(r'^(?P<codigo>[A-Z0-9]+)/handle/$', views.handle, name='handle'),
    url(r'^(?P<codigo>[A-Z0-9]+)/borrar/$', views.BorrarProducto.as_view(), name='borrar'),
    url(r'^(?P<codigo>[A-Z0-9]+)/editar/$', views.EditarProducto.as_view(), name='editar'),
    url(r'^search$', views.SearchView.as_view(), name='search'),
    url(r'^crear/$', views.crear, name='crear'),
    ]
