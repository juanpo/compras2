__author__ = 'juan'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ProductosView.as_view(), name='productos'),
    url(r'^(?P<codigo>[A-Z0-9]+)/$', views.detail, name='detail'),
    url(r'^search/$', views.search, name='search'),
]
