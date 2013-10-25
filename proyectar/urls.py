from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from proyectar import views

urlpatterns = patterns('',
	#url(r'^$', views.inicio, name='inicio'),
	#url(r'^inicio$', views.inicio, name='inicio'),
	#url(r'^entrar$',views.entrar,name='entrar'),
	#url(r'^salir$',views.salir,name='salir'),
    url(r'^proyectar/(?P<idPresentacion>\d+)/$',views.getSlides,name='getSlides'),
    url(r'^proyeccion/$',views.proyeccion,name='proyeccion'),
   
    # Examples:
    # url(r'^$', 'servicionacidosvivos.views.home', name='home'),
    # url(r'^servicionacidosvivos/', include('servicionacidosvivos.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)