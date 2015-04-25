__author__ = 'juan'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<codigo>[A-Z0-9]+)/$', views.detail, name='detail'),
]
