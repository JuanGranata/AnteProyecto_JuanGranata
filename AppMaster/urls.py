
from django.urls import path
from AppMaster.views import *

urlpatterns = [
   
    path("", inicio, name="inicio"),
    path("exitoso/", exitoso, name="exitoso"),
    path("buscar/", buscar, name="buscar"),
    path("empleado/", emple_form, name="empleado"),
    path("producto/", prod_form, name="producto"),
    path("cliente/", cli_form, name="cliente"),
    path("busquedaCliente/", busquedaCliente, name="busquedaCliente"),

]