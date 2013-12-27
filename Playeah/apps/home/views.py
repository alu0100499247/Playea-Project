from django.shortcuts import render_to_response
from django.template import RequestContext
from Playeah.apps.Playeah.models import playa
from Playeah.apps.home.forms import ContactForm
from django.core.mail import EmailMultiAlternatives	# Envio HTML

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

def contacto_view(request):
	info_enviado = False	
	email = ""
	titulo = ""
	texto = ""
	if request.method == "POST":
		formulario = ContactForm(request.POST)
		if formulario.is_valid():
			info_enviado = True
			email = formulario.cleaned_data['Email']
			titulo = formulario.cleaned_data['Titulo']
			texto = formulario.cleaned_data['Texto']

			# Configuracion del envio de correo (GMAIL)
			to_admin = "playeah.ull@gmail.com"
			html_content = "<h2>> %s</h2><br><br><strong>>> De:</strong> [%s] <br><br><strong>>> Mensaje:</strong><br><br><h2><em>%s</h2></em>"%(titulo,email,texto)
			msg = EmailMultiAlternatives('Correo de contacto',html_content,'from@server.com',[to_admin])
			msg.attach_alternative(html_content,'text/html')
			msg.send()
	else:
		formulario = ContactForm()
	ctx = {'form':formulario,'email':email,'titulo':titulo,'texto':texto,'info_enviado':info_enviado}
	return render_to_response('home/contacto.html',ctx,context_instance=RequestContext(request))

