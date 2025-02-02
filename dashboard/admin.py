from django.contrib import admin

from dashboard.models import Veiculo, Status_Veiculo, CustomUser, StatusUsuario, TipoUsuario, Estado,Forma_Pagamento,Reservas,Status_Reserva,Status_Uso

# Register your models here.
@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    ...
@admin.register(Status_Veiculo)
class Status_VeiculoAdmin(admin.ModelAdmin):
    ...
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    ...
    list_display = ('nome', 'email', 'cpf', 'telefone', 'tipo_usuario', 'status_usuario', 'date_joined', 'is_superuser','last_login')
@admin.register(StatusUsuario)
class StatusUsuarioAdmin(admin.ModelAdmin):
    ...
@admin.register(TipoUsuario)
class TipoUsuarioAdmin(admin.ModelAdmin):
    ...
@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    ...
@admin.register(Status_Reserva)
class StatusReservaAdmin(admin.ModelAdmin):
    ...

@admin.register(Forma_Pagamento)
class FormaPagamentoAdmin(admin.ModelAdmin):
    ...

@admin.register(Reservas)
class ReservasAdmin(admin.ModelAdmin):
    ...

@admin.register(Status_Uso)
class StatusUsoAdmin(admin.ModelAdmin):
    ...