from django.shortcuts import render_to_response
from django.template import RequestContext
from Playeah.apps.Playeah.models import playa
from Playeah.apps.home.forms import ContactForm, LoginForm, RegisterForm
from django.core.mail import EmailMultiAlternatives	# Envio HTML
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.models import User

def index_view(request):
	return render_to_response('home/index.html',context_instance=RequestContext(request))

def about_view(request):
	mensaje = "Esto es un mensaje desde mi vista"
	ctx = {'msg':mensaje}
	return render_to_response('home/about.html',ctx,context_instance=RequestContext(request))

def playas_view(request, pagina):
	playita = playa.objects.filter(status=True) # Select * from Playeah_playas where status = True
	paginator = Paginator(playita, 5)			# Playas por pagina
	try:
		page = int(pagina)						# Pasamos la variable pagina a entero
	except:
		page = 1								# En caso de que pasen un valor erroneo
	try:
		playas = paginator.page(page)			# Devuelve la pagina numero "page"
	except (EmptyPage, InvalidPage):
		playas = paginator.page(paginator.num_pages)	# Redireccionamos a la ultima pagina
	ctx = {'playas':playas}
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

def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				usuario = authenticate(username=username,password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect('/')
				else:
					mensaje = "Usuario y/o Password incorrecto."
		form = LoginForm()
		ctx = {'form':form,'mensaje':mensaje}
		return render_to_response('home/login.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def SinglePlaya_view(request, id_playa):
	playita = playa.objects.get(id=id_playa)
	categoria = playita.categorias.all()
	deporte = playita.deportes.all()
	cercania = playita.cercanias.all()
	bandera = playita.banderas
	ctx = {'playa':playita,'categorias':categoria,'deportes':deporte,'cercanias':cercania,'banderas':bandera}
	return render_to_response('home/SinglePlaya.html',ctx,context_instance=RequestContext(request))

def register_view(request):
	form = RegisterForm()
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			usuario = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password_one = form.cleaned_data['password_one']
			password_two = form.cleaned_data['password_two']
			u = User.objects.create_user(username=usuario,email=email,password=password_one)
			u.save()
			return render_to_response("home/thanks_register.html" ,context_instance=RequestContext(request))
		else:
			ctx = {'form':form}
			return render_to_response('home/register.html' ,ctx,context_instance=RequestContext(request))
	ctx = {'form':form}
	return render_to_response('home/register.html' ,ctx,context_instance=RequestContext(request))