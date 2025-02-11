from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Estado, TipoUsuario, StatusUsuario, Status_Veiculo, Forma_Pagamento

@receiver(post_migrate)
def criar_registros_padrao(sender, **kwargs):
    if sender.name == "dashboard":  # Apenas para o app "dashboard"
        estados_padrao = [
            {"sigla": "AC"},{"sigla": "AL"},{"sigla": "AP"},{"sigla": "AM"},
            {"sigla": "BA"},{"sigla": "CE"},{"sigla": "DF"},{"sigla": "ES"},
            {"sigla": "GO"},{"sigla": "MA"},{"sigla": "MT"},{"sigla": "MS"},
            {"sigla": "MG"},{"sigla": "PA"},{"sigla": "PB"},{"sigla": "PR"},
            {"sigla": "PE"},{"sigla": "PI"},{"sigla": "RJ"},{"sigla": "RN"},
            {"sigla": "RS"},{"sigla": "RO"},{"sigla": "RR"},{"sigla": "SC"},
            {"sigla": "SP"},{"sigla": "SE"},{"sigla": "TO"},
        ]
        for estado in estados_padrao:
            Estado.objects.get_or_create(sigla=estado["sigla"])

        TipoUsuario.objects.get_or_create(nome="ADMIN")
        TipoUsuario.objects.get_or_create(nome="Cliente")
        StatusUsuario.objects.get_or_create(status="Ativo")
        StatusUsuario.objects.get_or_create(status="Inatico")

        status_list = [
            {"status": "Disponível"},{"status": "Reservados"},{"status": "Em Uso"},
            {"status": "Atrasado"},{"status": "Manutenção"}
        ]
        for status_ in status_list:
            Status_Veiculo.objects.get_or_create(status=status_["status"])

        pagamentos_list = [
            {"status": "Cartão de Crédito"},{"status": "Cartão de Débito"},{"status": "PIX"},
            {"status": "Boleto Bancário"},{"status": "Trandferência Bancária"}
        ]
        for forma in pagamentos_list:
            Forma_Pagamento.objects.get_or_create(forma_pagamento=forma["status"])
        