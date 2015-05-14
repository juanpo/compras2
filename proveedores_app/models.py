from django.db import models

# Create your models here.

class Proveedor(models.Model):
	codigo = models.CharField(max_length=4, primary_key=True)
	descripcion = models.CharField(max_length=20)
