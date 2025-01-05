from django.contrib import admin
from .models import Usuario, StatusUsuario, TipoUsuario, Estado
# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    ...
    list_display = ('nome', 'email', 'cpf', 'telefone', 'tipo_usuario', 'status_usuario')


@admin.register(StatusUsuario)
class StatusUsuarioAdmin(admin.ModelAdmin):
    list_display = ('status','id')
    ...


@admin.register(TipoUsuario)
class TipoUsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome','id')
    ...


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    ...