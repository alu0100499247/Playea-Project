from django import forms
from Playeah.apps.Playeah.models import playa

class addPlayaForm(forms.ModelForm):
	class Meta:
		model 	= playa
		exclude = {'status'}
