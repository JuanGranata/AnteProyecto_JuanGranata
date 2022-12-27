from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from AppMaster.forms import *
from django.shortcuts import render

# Create your views here.

# Modulo de inicio
def inicio(request):
    return render (request, "AppMaster/inicio.html")

# Modulo mensaje exitoso
def exitoso(request):
    return render (request, "AppMaster/exitoso.html")

# Modulo carga de formulario de productos
def prod_form(request):
    if request.method=="POST":
        form=ProdForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            prod = Producto(codigo=data["codigo"], descripcion=data["descripcion"], cant=data["cant"])
            prod.save()
            return render (request, 'AppMasterexitoso.html', {"mensaje": "PRODUCTO CREADO CORRECTAMENTE!!"})
    else:
        formulario=ProdForm()
    
    return render (request, 'AppMaster/producto.html', {'form':formulario})

# Modulo carga de formulario de empleados
def emple_form(request):
    if request.method=="POST":
        form=EmpForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            emple = Empleado(nombre=info["nombre"], apellido=info["apellido"], fecha_nac=info["fecha_nac"], dni=info["dni"], email=info["email"], cargo=info["cargo"])
            emple.save()
            return render (request, "AppMaster/exitoso.html", {"mensaje": "EMPLEADO CREADO CORRECTAMENTE!!"})
    else:
        formulario=EmpForm()

    return render (request, "AppMaster/empleado.html", {"form":formulario})

# Modulo carga de clientes
def cli_form(request):
    if request.method=="POST":
        form=CliForm(request.POST)
        if form.is_valid():
            cli = form.cleaned_data
            cliente = Cliente(cliente=cli["cliente"], direccion=cli["direccion"], pedido=cli["pedido"],estado=cli["estado"])
            cliente.save()
            return render (request, 'AppMaster/exitoso.html', {"mensaje": "CLIENTE CREADO CORRECTAMENTE!!"})
    else:
        formulario=CliForm()
    
    return render (request, 'AppMaster/cliente.html', {'form':formulario})

# Modulos de buquedas de clinetes en la base de datos
def busquedaCliente(request):
    return render(request, "AppMaster/busquedaCliente.html")

# Algoritmo de busqueda de cliente
def buscar(request):

    if request.GET["cliente"]:

        cliente=request.GET["cliente"]
        clientes=Cliente.objects.filter(cliente__icontains=cliente)
        return render(request,"AppMaster/resultadosBusqueda.html", {"clientes":clientes} )
    
    else:
        return render(request, "AppMaster/busquedaCliente.html", {"mensaje":"Por favor ingresa el cliente"})








