from django.db import models

# Create your models here.
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    
class Vendedor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    
class Vehiculo(models.Model):
    modelo_vehiculo = models.CharField(max_length=30)
    ano_vehiculo = models.IntegerField()
    precio = models.IntegerField()
    
class VehiculoStock(models.Model):
    modelo_vehiculo = models.CharField(max_length=30)
    ano_vehiculo = models.IntegerField()
    precio = models.IntegerField()
    disponible = models.BooleanField()
    