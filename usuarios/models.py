from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.apps import apps

class TipoUsuario(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class StatusUsuario(models.Model):
    status = models.CharField(max_length=35)

    def __str__(self):
        return self.status


class CustomUser(AbstractUser):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=15)
    rua = models.CharField(max_length=35)
    bairro = models.CharField(max_length=35)
    cidade = models.CharField(max_length=35)
    cep = models.CharField(max_length=15)
    imagem = models.ImageField(
        upload_to="imagens/usuario",
        height_field=None,
        width_field=None,
        max_length=None,
        default="carro-escondido.jpg",
    )
    estado = models.ForeignKey('dashboard.Estado', on_delete=models.CASCADE, null=True, blank=True)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE, null=True, blank=True)
    status_usuario = models.ForeignKey(StatusUsuario, on_delete=models.CASCADE, null=True, blank=True)
  # Evita conflitos nos relacionamentos do Django
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_set",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions_set",
        blank=True
    )

    data_cadastro = models.DateField(auto_now_add=True, verbose_name="Data de Cadastro")
    data_alteracao = models.DateField(auto_now=True, verbose_name="Data de Alteração")
    usuario_cadastro = models.ForeignKey(
         settings.AUTH_USER_MODEL,
         on_delete=models.SET_NULL,
         null=True,
         blank=True,
         related_name="usuarios_cadastrados",
         verbose_name="Usuário Cadastro"
    )
    usuario_alteracao = models.ForeignKey(
         settings.AUTH_USER_MODEL,
         on_delete=models.SET_NULL,
         null=True,
         blank=True,
         related_name="usuarios_alterados",
         verbose_name="Usuário Alteração"
    )

    def __str__(self):
        return self.nome

