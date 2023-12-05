from django.shortcuts import render
from django.shortcuts import redirect
from django.template import Template, Context
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def index(self):
    mihtml = open("AppDB/templates/index.html")
    plantilla = Template(mihtml.read())
    mihtml.close()
    micontexto = Context()
    documento = plantilla.render(micontexto)
    
    return HttpResponse(documento)

def registrado(self):
    mihtml = open("AppDB/templates/registrado.html")
    plantilla = Template(mihtml.read())
    mihtml.close()
    micontexto = Context()
    documento = plantilla.render(micontexto)
    
    return HttpResponse(documento)

def NuestrosVehiculos(self):
    vehiculos = Vehiculo.objects.all()
    mihtml = open("AppDB/templates/nuestrosvehiculos.html")
    plantilla = Template(mihtml.read())
    mihtml.close()
    micontexto = Context({"Vehiculos":list(vehiculos)})
    documento = plantilla.render(micontexto)
    
    return HttpResponse(documento)

#def Vender(self):
#    mihtml = open("AppDB/templates/vender.html")
#    plantilla = Template(mihtml.read())
#    mihtml.close()
#    micontexto = Context()
#    documento = plantilla.render(micontexto)
#    
#    return HttpResponse(documento)

#def Registrarse(self):
#    mihtml = open("AppDB/templates/vender.html")
#    plantilla = Template(mihtml.read())
#    mihtml.close()
#    micontexto = Context()
#    documento = plantilla.render(micontexto)
#    
#    return HttpResponse(documento)

def vender_formulario(request):
    if request.method == "POST":
        form = VenderVehiculo(request.POST)
        if form.is_valid():
            Vehiculo = form.save()
            return redirect("/")
    else:
        form = VenderVehiculo()
        
    return render(request, "vender.html", {"form":form})

def registrarse_formulario(request):
    if request.method == "POST":
        form = Registrarse_Cliente(request.POST)
        if form.is_valid():
            Vehiculo = form.save()
            return redirect("http://127.0.0.1:8000/Registrado/")
    else:
        form = Registrarse_Cliente()
        
    return render(request, "registrarse.html", {"form":form})