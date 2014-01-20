from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('Playeah.apps.home.views',
	url(r'^$','index_view',name='vista_principal'),
	url(r'^about/$','about_view',name='vista_about'),
	url(r'^playas/page/(?P<pagina>.*)/$','playas_view',name='vista_playas'),
	url(r'^contacto/$','contacto_view',name='vista_contacto'),
	url(r'^login/$','login_view',name='vista_login'),
	url(r'^logout/$','logout_view',name='vista_logout'),
	url(r'^registro/$','register_view',name='vista_registro'),
	url(r'^playa/(?P<id_playa>.*)/$','SinglePlaya_view',name='vista_single_playa'),
)