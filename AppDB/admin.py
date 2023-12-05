from django.contrib import admin
from AppDB import models

# Register your models here.

admin.site.register(models.Cliente)
admin.site.register(models.Vendedor)
admin.site.register(models.Vehiculo)
@admin.register(models.VehiculoStock)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ("modelo_vehiculo", "ano_vehiculo", "precio")
    list_filter = ("modelo_vehiculo", "precio")
    search_fields = ("modelo_vehiculo", "precio")