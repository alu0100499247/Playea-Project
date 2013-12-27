from django.shortcuts import render_to_response
from django.template import RequestContext
from Playeah.apps.Playeah.forms import addPlayaForm
from Playeah.apps.Playeah.models import playa

def add_playa_view(request):
	if request.method == "POST":
		form = addPlayaForm(request.POST)
		info = "Inicializando"
		if form.is_valid():
			nombre = form.cleaned_data['nombre']
			ubicacion = form.cleaned_data['ubicacion']
			descripcion = form.cleaned_data['descripcion']
			p = playa()
			p.nombre = nombre
			p.ubicacion = ubicacion
			p.descripcion = descripcion
			p.status = True
			p.save()	# Guardamos la informacion
			info = "La playa ha sido almacenada correctamente."
		else:
			info = "Informacion con datos incorrectos."
		form = addPlayaForm()
		ctx = {'form':form,'informacion':info}
		return render_to_response('Playeah/addPlaya.html',ctx,context_instance=RequestContext(request))
	
	else:	# GET
		form = addPlayaForm()
		ctx = {'form':form}
		return render_to_response('Playeah/addPlaya.html',ctx,context_instance=RequestContext(request))
