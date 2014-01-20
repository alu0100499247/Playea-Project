from django.shortcuts import render_to_response
from django.template import RequestContext
from Playeah.apps.Playeah.forms import addPlayaForm
from Playeah.apps.Playeah.models import playa
from django.http import HttpResponseRedirect

def add_playa_view(request):
	if request.method == "POST":
		form = addPlayaForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.status = True
			add.save()
			form.save_m2m() 	# Guarda los ManyToMany
			return HttpResponseRedirect('/playa/%s/'%add.id)
	else:
		form = addPlayaForm()
	ctx = {'form':form}
	return render_to_response('Playeah/addPlaya.html',ctx,context_instance=RequestContext(request))

def edit_playa_view(request, id_playa):
	playita = playa.objects.get(pk=id_playa)
	if request.method == "POST":
		form = addPlayaForm(request.POST,request.FILES,instance=playita)
		if form.is_valid():
			edit = form.save(commit=False)
			edit.status = True
			edit.save()
			form.save_m2m()
			return HttpResponseRedirect('/playa/%s/'%edit.id)
	else:
		form = addPlayaForm(instance=playita)
	ctx = {'form':form}
	return render_to_response('Playeah/editPlaya.html',ctx,context_instance=RequestContext(request))

