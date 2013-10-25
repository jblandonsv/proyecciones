# Create your views here.
import json
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.conf import settings

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from proyectar.models import Presentacion,Slides

def getSlides(request,idPresentacion):
	p = Presentacion.objects.filter(pk=idPresentacion)
	slides = Slides.objects.filter(presentacion=p)
	presentacion = {'nombre':p[0].nombre,'autor':p[0].autor,'descripcion':p[0].descripcion,'slides':slides,
					'url_path':settings.MEDIA_URL}

	return render_to_response('slides.html',{'presentacion':presentacion},context_instance = RequestContext(request))

def proyeccion(request):
	return render_to_response('proyecciones.html',None,context_instance = RequestContext(request))