from django.db import models

# Create your models here.
# Creacion de modelos para la base de datos

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    dni = models.IntegerField()
    email = models.EmailField()
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+" "+self.apellido

class Producto(models.Model):
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=50)
    cant = models.IntegerField()

    def __str__(self):
        return self.descripcion

class Cliente(models.Model):
    cliente = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    pedido = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.cliente+" "+self.estado