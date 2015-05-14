__author__ = 'juan'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ProveedoresView.as_view(), name='proveedores'),
    url(r'^search$', views.ProveedoresSearchView.as_view(), name='search'),    
    url(r'^(?P<codigo>[A-Z0-9]+)/$', views.ProveedoresDetalleView.as_view(), name='detail'),
    url(r'^(?P<codigo>[A-Z0-9]+)/handle/$', views.handle, name='handle'),
    url(r'^(?P<codigo>[A-Z0-9]+)/borrar/$', views.ProveedoresBorrarView.as_view(), name='borrar'),
    url(r'^(?P<codigo>[A-Z0-9]+)/editar/$', views.ProveedoresEditarView.as_view(), name='editar'),
    url(r'^crear/$', views.ProveedoresCrearView.as_view(), name='crear'),
    ]