from django.db import models

class usuario(models.Model):
	nombre		= models.CharField(max_length=200)
	apellidos	= models.CharField(max_length=200)
	status		= models.BooleanField(default=True)

	def __unicode__(self):
		NombreCompleto = "%s %s"%(self.nombre, self.apellidos)
		return NombreCompleto

class categoria(models.Model):
	nombre 		= models.CharField(max_length=200)
	descripcion = models.TextField(max_length=500)

	def __unicode__(self):
		return self.nombre

class deporte(models.Model):
	nombre 		= models.CharField(max_length=200)
	descripcion = models.TextField(max_length=500)

	def __unicode__(self):
		return self.nombre

class cercania(models.Model):
	nombre 		= models.CharField(max_length=200)
	descripcion = models.TextField(max_length=500)

	def __unicode__(self):
		return self.nombre

class bandera(models.Model):
	nombre 		= models.CharField(max_length=200)
	descripcion = models.TextField(max_length=500)

	def __unicode__(self):
		return self.nombre

class playa(models.Model):

	def url(self, filename):
		ruta = "MultimediaData/Playa/%s/%s"%(self.nombre,str(filename))
		return ruta

	nombre		= models.CharField(max_length=200)
	ubicacion	= models.CharField(max_length=200)
	descripcion	= models.TextField(max_length=2000)
	status		= models.BooleanField(default=True)
	imagen		= models.ImageField(upload_to=url,null=True,blank=True)
	categorias	= models.ManyToManyField(categoria,null=True,blank=True)
	deportes	= models.ManyToManyField(deporte,null=True,blank=True)
	cercanias	= models.ManyToManyField(cercania,null=True,blank=True)
	banderas	= models.OneToOneField(bandera,null=True,blank=True)

	def __unicode__(self):
		return self.nombre
