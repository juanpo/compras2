from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    descripcion = models.CharField(max_length=100)


    def __str__(self):
        return self.descripcion








		
		

