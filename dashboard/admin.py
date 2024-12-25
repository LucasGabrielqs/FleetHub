from django.contrib import admin
from .models import Usuário, StatusUsuario, TipoUsuario, Estado
# Register your models here.
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