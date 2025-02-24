from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Estado, TipoUsuario, StatusUsuario

@receiver(post_migrate)
def criar_registros_padrao(sender, **kwargs):
    if sender.name == "usuarios":  # Apenas para o app "dashboard"
    
        TipoUsuario.objects.get_or_create(nome="ADMIN")
        TipoUsuario.objects.get_or_create(nome="Cliente")

        StatusUsuario.objects.get_or_create(status="Ativo")
        StatusUsuario.objects.get_or_create(status="Inativo")


        