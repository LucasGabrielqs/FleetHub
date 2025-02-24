from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Status_Veiculo

@receiver(post_migrate)
def criar_registros_padrao(sender, **kwargs):
    if sender.name == "veiculos":  # Apenas para o app "dashboard"

        status_list = [
            {"status": "Disponível", "status_cor":"34C759"},{"status": "Reservados", "status_cor":"007AFF"},
            {"status": "Em Uso", "status_cor":"FFCC00"},
            {"status": "Atrasado", "status_cor":"FF3B30"},{"status": "Manutenção", "status_cor":"625E5E"}
        ]
        for status_ in status_list:
            Status_Veiculo.objects.get_or_create(status=status_["status"], status_cor=status_["status_cor"])

        