from django import forms

# Creacion de los formatos para las tablas dinamicas a ser usadas en los HTMLs

class ProdForm(forms.Form):
    codigo = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length=50)
    cant = forms.IntegerField()

class EmpForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    fecha_nac = forms.DateField()
    dni = forms.IntegerField()
    email = forms.EmailField()
    cargo = forms.CharField(max_length=50)

class CliForm(forms.Form):
    cliente = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=50)
    pedido = forms.CharField(max_length=50)
    estado = forms.CharField(max_length=50)

