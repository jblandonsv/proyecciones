from django.db import models

# Create your models here.
class Presentacion(models.Model):
	nombre = models.CharField(blank=False,max_length=500)
	autor = models.CharField(blank=False,max_length=600)
	descripcion = models.TextField(blank=False)

	def __unicode__(self):
		return self.nombre

class Slides(models.Model):
	nombre = models.CharField(blank=False,unique=True,max_length=140)
	imagen = models.ImageField(blank=False,upload_to='imagenes')
	presentacion = models.ForeignKey(Presentacion)

	def __unicode__(self):
		return self.nombre