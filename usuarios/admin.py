from django.contrib import admin
from usuarios.models import CustomUser,StatusUsuario,TipoUsuario

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    ...
    list_display = ('nome', 'email', 'cpf', 'telefone', 'tipo_usuario', 'status_usuario', 'date_joined', 'is_superuser','last_login')
@admin.register(StatusUsuario)
class StatusUsuarioAdmin(admin.ModelAdmin):
    list_display = ('id','status')
    ...
@admin.register(TipoUsuario)
class TipoUsuarioAdmin(admin.ModelAdmin):
    ...
    list_display = ('id','nome')