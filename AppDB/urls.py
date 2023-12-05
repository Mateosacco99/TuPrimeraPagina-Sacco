from django.urls import path
from .views import *

urlpatterns = [
    path("", index,),
    path("NuestrosVehiculos/", NuestrosVehiculos),
    path("Vender/", vender_formulario),
    path("Registrado/", registrado),
    path("Registrarse/", registrarse_formulario),
]
