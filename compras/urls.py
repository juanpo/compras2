from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'compras.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', RedirectView.as_view(url='/productos/')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^productos/', include('compras_app.urls', namespace="compras_app")),
    url(r'^proveedores/', include('proveedores_app.urls', namespace="proveedores_app")),

    
)
