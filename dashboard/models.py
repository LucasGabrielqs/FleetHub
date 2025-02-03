from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.conf import settings

class TipoUsuario(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Estado(models.Model):
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return self.sigla


class StatusUsuario(models.Model):
    status = models.CharField(max_length=35)

    def __str__(self):
        return self.status


class CustomUser(AbstractUser):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=15)
    #senha = models.CharField(max_length=128)
    #data_cadastro = models.DateField(auto_now=True)
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
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.SET_DEFAULT, default="indefinido")
    status_usuario = models.ForeignKey(StatusUsuario, on_delete=models.SET_DEFAULT, default="indefinido")
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

    # data_cadastro = models.DateField(auto_now_add=True, verbose_name="Data de Cadastro")
    # data_alteracao = models.DateField(auto_now=True, verbose_name="Data de Alteração")
    # usuario_cadastro = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    #     related_name="usuarios_cadastrados",
    #     verbose_name="Usuário Cadastro"
    # )
    # usuario_alteracao = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    #     related_name="usuarios_alterados",
    #     verbose_name="Usuário Alteração"
    # )

    def __str__(self):
        return self.nome


class Status_Veiculo(models.Model):
    status = models.CharField(max_length=50, default="Indefinido")

    def __str__(self):
        return self.status


class Status_Uso(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=100)
    valor_compra = models.CharField(max_length=25)
    ano = models.IntegerField()
    km = models.CharField(max_length=20)
    motor = models.CharField(max_length=10)
    placa = models.CharField(max_length=20)
    chassi = models.CharField(max_length=20)
    cor = models.CharField(max_length=50, default="indefinido")
    imagem = models.ImageField(
        upload_to="imagens/veiculos",
        height_field=None,
        width_field=None,
        max_length=None,
        default="media/carro-escondido.jpg",
    )
    status = models.ForeignKey(Status_Veiculo, on_delete=models.CASCADE, related_name="veiculos_status")
    #status_uso = models.ForeignKey(Status_Uso, on_delete=models.CASCADE, related_name="veiculos_status_uso")
    data_cadastro = models.DateField(auto_now_add=True)
    data_alteracao = models.DateField(auto_now=True)
    usuario_cadastro = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="veiculos_cadastrados",
    )
    usuario_alteracao = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="veiculos_alterados",
    )

    def __str__(self):
        return self.modelo


class Forma_Pagamento(models.Model):
    forma_pagamento = models.CharField(max_length=30, default="Indefinido")

    def __str__(self):
        return self.forma_pagamento


class Status_Reserva(models.Model):
    status = models.CharField(max_length=50, default="Indefinido")

    def __str__(self):
        return self.status


class Reservas(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name="reservas")
    data_reserva = models.DateField()
    data_entrega = models.DateField()
    motorista = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="reservas_como_motorista",
    )
    idade_condutor = models.IntegerField()
    valor = models.FloatField()
    forma_pagamento = models.CharField(max_length=30)
    status_reserva = models.ForeignKey(Status_Reserva, on_delete=models.CASCADE, related_name="reservas_status")
    data_cadastro = models.DateField(auto_now_add=True)
    data_alteracao = models.DateField(auto_now=True)
    usuario_cadastro = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reservas_cadastradas",
    )
    usuario_alteracao = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reservas_alteradas",
    )

    def __str__(self):
        return f"Reserva {self.id} - {self.veiculo.modelo}"
