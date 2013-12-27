from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('Playeah.apps.Playeah.views',
	url(r'^add/playa/$','add_playa_view',name='vista_agregar_playa'),
)