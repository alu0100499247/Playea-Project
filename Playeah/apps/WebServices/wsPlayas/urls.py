from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('Playeah.apps.WebServices.wsPlayas.views',
	url(r'^ws/playas/$','wsPlayas_view',name='ws_playas_url'),
)