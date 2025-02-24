from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from dashboard.models import  Forma_Pagamento,Reservas,Status_Reserva,Abastecimento,Tipo_Combustivel,Manutencao,Prioridade_Atendimento,Tipo_Manutencao, Status_Manutencao,Tipo_Carga,Rota

# Register your models here.


@admin.register(Status_Reserva)
class StatusReservaAdmin(admin.ModelAdmin):
    list_display = ('id',"status")
    ...

@admin.register(Forma_Pagamento)
class FormaPagamentoAdmin(admin.ModelAdmin):
    ...

@admin.register(Reservas)
class ReservasAdmin(admin.ModelAdmin):
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

@admin.register(Tipo_Carga)
class Tipo_CargaAdmin(admin.ModelAdmin):
    ...


@admin.register(Rota)
class RotaAdmin(admin.ModelAdmin):
    ...