__author__ = 'juan'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ProductosView.as_view(), name='productos'),
    url(r'^(?P<codigo>[A-Z0-9]+)/$', views.detail, name='detail'),
    url(r'^search$', views.SearchView.as_view(), name='search'),
    url(r'^crear/$', views.crear, name='crear'),
    url(r'^borrar/$', views.BorrarProducto.as_view(), name='borrar'),
    ]
