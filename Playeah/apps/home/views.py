from django.shortcuts import render_to_response
from django.template import RequestContext
from Playeah.apps.Playeah.models import playa

def index_view(request):
	return render_to_response('home/index.html',context_instance=RequestContext(request))

def about_view(request):
	mensaje = "Esto es un mensaje desde mi vista"
	ctx = {'msg':mensaje}
	return render_to_response('home/about.html',ctx,context_instance=RequestContext(request))

def playas_view(request):
	playita = playa.objects.filter(status=True) # Select * from Playeah_playas where status = True
	ctx = {'playas':playita}
	return render_to_response('home/playas.html',ctx,context_instance=RequestContext(request))

