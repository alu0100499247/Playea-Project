from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('Playeah.apps.home.views',
	url(r'^$','index_view',name='vista_principal'),
	url(r'^about/$','about_view',name='vista_about'),
	url(r'^playas/$','playas_view',name='vista_playas'),
	url(r'^contacto/$','contacto_view',name='vista_contacto'),
)