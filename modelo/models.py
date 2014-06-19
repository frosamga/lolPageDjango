from django.db import models

class Region(models.Model):
	nombre_region=models.CharField(max_length=60)
	descripcion_region=models.CharField(max_length=200)

class Campeon(models.Model):
	nombre_campeon=models.CharField(max_length=60)
	descripcion_campeon=models.CharField(max_length=200)
	kill=models.IntegerField()
	death=models.IntegerField()
	assistances=models.IntegerField()
	imagen=models.FileField(upload_to='fotos')
	region=models.ForeignKey(Region,blank=True)
