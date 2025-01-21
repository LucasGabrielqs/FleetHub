from django.contrib import admin

from dashboard.models import Veiculo, Status_Veiculo

# Register your models here.
@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    ...

@admin.register(Status_Veiculo)
class Status_VeiculoAdmin(admin.ModelAdmin):
    ...