from django.shortcuts import render_to_response
from django.template import RequestContext
from Playeah.apps.Playeah.forms import addPlayaForm
from Playeah.apps.Playeah.models import playa
from django.http import HttpResponseRedirect

def add_playa_view(request):
	info = "Inicializando"
	if request.user.is_authenticated():
		if request.method == "POST":
			form = addPlayaForm(request.POST,request.FILES)
			if form.is_valid():
				nombre = form.cleaned_data['nombre']
				ubicacion = form.cleaned_data['ubicacion']
				descripcion = form.cleaned_data['descripcion']
				imagen = form.cleaned_data['imagen'] 	# Esto se obtiene con el request.FILES
				p = playa()
				if imagen:	# Generamos una validacion
					p.imagen = imagen
				p.nombre 		= nombre
				p.ubicacion 	= ubicacion
				p.descripcion 	= descripcion
				p.status = True
				p.save()	# Guardamos la informacion
				info = "La playa ha sido almacenada correctamente."
			else:
				info = "Informacion con datos incorrectos."
		form = addPlayaForm()
		ctx = {'form':form,'informacion':info}
		return render_to_response('Playeah/addPlaya.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')
	