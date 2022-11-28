from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from AppCoder.forms import *
from django.shortcuts import render

# Create your views here.

# Modulo de inicio
def inicio(request):
    return render (request, "AppCoder/inicio.html")

# Modulo mensaje exitoso
def exitoso(request):
    return render (request, "AppCoder/exitoso.html")

# Modulo carga de formulario de productos
def prod_form(request):
    if request.method=="POST":
        form=ProdForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            prod = Producto(codigo=data["codigo"], descripcion=data["descripcion"], cant=data["cant"])
            prod.save()
            return render (request, 'AppCoder/exitoso.html', {"mensaje": "PRODUCTO CREADO CORRECTAMENTE!!"})
    else:
        formulario=ProdForm()
    
    return render (request, 'AppCoder/producto.html', {'form':formulario})

# Modulo carga de formulario de empleados
def emple_form(request):
    if request.method=="POST":
        form=EmpForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            emple = Empleado(nombre=info["nombre"], apellido=info["apellido"], fecha_nac=info["fecha_nac"], dni=info["dni"], email=info["email"], cargo=info["cargo"])
            emple.save()
            return render (request, "AppCoder/exitoso.html", {"mensaje": "EMPLEADO CREADO CORRECTAMENTE!!"})
    else:
        formulario=EmpForm()

    return render (request, "AppCoder/empleado.html", {"form":formulario})

# Modulo carga de clientes
def cli_form(request):
    if request.method=="POST":
        form=CliForm(request.POST)
        if form.is_valid():
            cli = form.cleaned_data
            cliente = Cliente(cliente=cli["cliente"], direccion=cli["direccion"], pedido=cli["pedido"],estado=cli["estado"])
            cliente.save()
            return render (request, 'AppCoder/exitoso.html', {"mensaje": "CLIENTE CREADO CORRECTAMENTE!!"})
    else:
        formulario=CliForm()
    
    return render (request, 'AppCoder/cliente.html', {'form':formulario})

# Modulos de buquedas de clinetes en la base de datos
def busquedaCliente(request):
    return render(request, "Appcoder/busquedaCliente.html")

# Algoritmo de busqueda de cliente
def buscar(request):

    if request.GET["cliente"]:

        cliente=request.GET["cliente"]
        clientes=Cliente.objects.filter(cliente__icontains=cliente)
        return render(request,"AppCoder/resultadosBusqueda.html", {"clientes":clientes} )
    
    else:
        return render(request, "AppCoder/busquedaCliente.html", {"mensaje":"Por favor ingresa el cliente"})








