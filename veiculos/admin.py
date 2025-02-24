from django.contrib import admin
from .models import Status_Veiculo,Veiculo,Tipo_Veiculo

# Register your models here.
@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    ...
@admin.register(Status_Veiculo)
class Status_VeiculoAdmin(admin.ModelAdmin):
    list_display = ("id","status")
    ...

@admin.register(Tipo_Veiculo)
class Tipo_VeiculoAdmin(admin.ModelAdmin):
    list_display = ("id","tipo")