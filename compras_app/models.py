from django.db import models

# Create your models here.

class Proveedor(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Orden(models.Model):
    proveedor = models.ForeignKey(Proveedor)
    fecha = models.DateField(auto_now=True)


    def __str__(self):
        return "Orden #" + str(self.id)


class Producto(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    descripcion = models.CharField(max_length=100)
    cantidad = models.IntegerField(default=0)
    orden = models.ForeignKey(Orden, null=True)

    def __str__(self):
        return self.descripcion




		
		

