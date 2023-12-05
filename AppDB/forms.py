from django import forms
from .models import Vehiculo
from .models import *

class VenderVehiculo(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ["modelo_vehiculo", "ano_vehiculo", "precio"]
        
class Registrarse_Cliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "apellido", "email"]