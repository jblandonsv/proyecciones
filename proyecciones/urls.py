from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
	url(r'^proyecciones/', include('proyectar.urls')),
    # Examples:
    # url(r'^$', 'proyecciones.views.home', name='home'),
    # url(r'^proyecciones/', include('proyecciones.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
