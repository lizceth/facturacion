from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    #url(r'^$', TemplateView.as_view(template_name='base.html')),

    # Examples:
    # url(r'^$', 'Factura.views.home', name='home'),
    # url(r'^Factura/', include('Factura.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^$','facturaciones.views.ingresar'),
    url(r'^privado/$','facturaciones.views.privado'),
#    url(r'^factura/$','facturaciones.views.privado'),
    url(r'^clientes$','facturaciones.views.clientes'),
    url(r'^clienteAdd/$','facturaciones.views.clienteAdd'),
    url(r'^clienteEdit/(?P<id>\d+)$','facturaciones.views.clienteEdit'),
    url(r'^clienteDelete/(?P<id>\d+)$','facturaciones.views.clienteDelete'),
    url(r'^productos/$','facturaciones.views.productos'),
    url(r'^productoAdd/$','facturaciones.views.productoAdd'),
    url(r'^productoEdit/(?P<id>\d+)$','facturaciones.views.productoEdit'),
    url(r'^productoDelete/(?P<id>\d+)$','facturaciones.views.productoDelete'),
    url(r'^factura/$','facturaciones.views.factura'),
    url(r'^detalle/$','facturaciones.views.detalle'),
    url(r'^imprimir/$', TemplateView.as_view(template_name='facturaciones/imprimir.html')),
    url(r'^cerrar/$','facturaciones.views.cerrar'),
)

# Uncomment the next line to serve media files in dev.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
