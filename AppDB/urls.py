from django.urls import path
from .views import *

urlpatterns = [
    path("", index),
    path("NuestrosVehiculos/", NuestrosVehiculos),
    path("Vender/", Vender),
    path("Registrarse/", Registrarse),
]
