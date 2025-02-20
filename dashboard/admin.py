from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from dashboard.models import Veiculo, Status_Veiculo, CustomUser, StatusUsuario, TipoUsuario, Estado,Forma_Pagamento,Reservas,Status_Reserva,Status_Uso,Abastecimento,Tipo_Combustivel,Manutencao,Prioridade_Atendimento,Tipo_Manutencao, Status_Manutencao

# Register your models here.
@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    ...
@admin.register(Status_Veiculo)
class Status_VeiculoAdmin(admin.ModelAdmin):
    list_display = ("id","status")
    ...
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

@admin.register(Tipo_Manutencao)
class Tipo_ManutencaoAdmin(admin.ModelAdmin):
    ...

@admin.register(Manutencao)
class ManutencaoAdmin(admin.ModelAdmin):
    ...

@admin.register(Abastecimento)
class AbastecimentoAdmin(admin.ModelAdmin):
    ...

@admin.register(Tipo_Combustivel)
class Tipo_CombustivelAdmin(admin.ModelAdmin):
    ...

@admin.register(Prioridade_Atendimento)
class Prioridade_AtendimentoAdmin(admin.ModelAdmin):
    ...

@admin.register(Status_Manutencao)
class Status_ManutencaoAdmin(admin.ModelAdmin):
    list_display = ("id","nome_status")
    ...
