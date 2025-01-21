from django.contrib import admin

from dashboard.models import Veiculo, Status_Veiculo, Usuário, StatusUsuario, TipoUsuario, Estado

# Register your models here.
@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    ...
@admin.register(Status_Veiculo)
class Status_VeiculoAdmin(admin.ModelAdmin):
    ...
@admin.register(Usuário)
class UsuarioAdmin(admin.ModelAdmin):
    ...
    list_display = ('nome', 'email', 'cpf', 'telefone', 'tipo_usuario', 'status_usuario')
@admin.register(StatusUsuario)
class StatusUsuarioAdmin(admin.ModelAdmin):
    ...
@admin.register(TipoUsuario)
class TipoUsuarioAdmin(admin.ModelAdmin):
    ...
@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    ...