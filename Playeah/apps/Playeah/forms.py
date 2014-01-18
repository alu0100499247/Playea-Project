from django import forms

class addPlayaForm(forms.Form):
	nombre 		= forms.CharField(widget=forms.TextInput())
	ubicacion 	= forms.CharField(widget=forms.TextInput())
	descripcion = forms.CharField(widget=forms.Textarea())
	imagen		= forms.ImageField(required=False)

	def clean(self):
		return self.cleaned_data