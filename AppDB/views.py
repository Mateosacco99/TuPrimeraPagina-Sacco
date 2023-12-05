from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse
from .models import VehiculoStock

# Create your views here.

def index(self):
    mihtml = open("C:/Users/mateo/OneDrive/Escritorio/MiPrimeraPagina/AppDB/templates/index.html")
    plantilla = Template(mihtml.read())
    mihtml.close()
    micontexto = Context()
    documento = plantilla.render(micontexto)
    
    return HttpResponse(documento)

def NuestrosVehiculos(self):
    vehiculos = VehiculoStock.objects.all()
    mihtml = open("C:/Users/mateo/OneDrive/Escritorio/MiPrimeraPagina/AppDB/templates/nuestrosvehiculos.html")
    plantilla = Template(mihtml.read())
    mihtml.close()
    micontexto = Context({"vehiculosstock":list(vehiculos)})
    documento = plantilla.render(micontexto)
    
    return HttpResponse(documento)

def Vender(self):
    vehiculos = VehiculoStock.objects.all()
    mihtml = open("C:/Users/mateo/OneDrive/Escritorio/MiPrimeraPagina/AppDB/templates/vender.html")
    plantilla = Template(mihtml.read())
    mihtml.close()
    micontexto = Context()
    documento = plantilla.render(micontexto)
    
    return HttpResponse(documento)

def Registrarse(self):
    vehiculos = VehiculoStock.objects.all()
    mihtml = open("C:/Users/mateo/OneDrive/Escritorio/MiPrimeraPagina/AppDB/templates/vender.html")
    plantilla = Template(mihtml.read())
    mihtml.close()
    micontexto = Context()
    documento = plantilla.render(micontexto)
    
    return HttpResponse(documento)