from django.http import HttpResponse
from Playeah.apps.Playeah.models import playa
from django.core import serializers

def wsPlayas_view(request):
	data = serializers.serialize("json",playa.objects.filter(status=True))
	return HttpResponse(data,mimetype='application/json')	# Devuelve la info en formato json