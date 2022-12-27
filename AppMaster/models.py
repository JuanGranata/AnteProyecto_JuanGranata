from django.db import models

# Create your models here.
# Creacion de modelos para la base de datos

class Usuario(models.Model):
    usuario = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.usuario+" "+self.email

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

#class Avatar(models.Model):
#    imagen=models.ImageField(upload_to='avatares')
#    user=models.ForeignKey(User, on_delete=models.CASCADE)
#
#    def __str__(self):
#        return f"{self.user} - {self.imagen}"