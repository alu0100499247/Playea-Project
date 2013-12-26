from django.db import models

class usuario(models.Model):
	nombre		= models.CharField(max_length=200)
	apellidos	= models.CharField(max_length=200)
	status		= models.BooleanField(default=True)

	def __unicode__(self):
		NombreCompleto = "%s %s"%(self.nombre, self.apellidos)
		return NombreCompleto

class playa(models.Model):
	nombre		= models.CharField(max_length=200)
	ubicacion	= models.CharField(max_length=200)
	descripcion	= models.TextField(max_length=800)
	status		= models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre
