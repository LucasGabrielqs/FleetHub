from django.contrib import admin

from dashboard.models import Veiculo

# Register your models here.
@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    ...