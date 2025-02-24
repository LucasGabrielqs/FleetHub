from django.db import models
from django.contrib.auth.models import AbstractUser
from veiculos.models import Veiculo,Tipo_Veiculo,Status_Veiculo
from django.apps import apps
# from django.conf import settings


class Estado(models.Model):
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return self.sigla

class Forma_Pagamento(models.Model):
    forma_pagamento = models.CharField(max_length=30, default="Indefinido")

    def __str__(self):
        return self.forma_pagamento


class Status_Reserva(models.Model):
    status = models.CharField(max_length=50, default="Indefinido")
    status_cor = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.status


class Reservas(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name="reservas")
    data_reserva = models.DateField()
    data_entrega = models.DateField()
    motorista = models.ForeignKey(
        'usuarios.CustomUser',
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
        'usuarios.CustomUser',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reservas_cadastradas",
    )
    usuario_alteracao = models.ForeignKey(
        'usuarios.CustomUser',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reservas_alteradas",
    )

    def __str__(self):
        return f"Reserva {self.id} - {self.veiculo.modelo}"
    
    def modificar_reserva(self,value):
        novo_status = Status_Reserva.objects.get(id=value) 
        self.status_reserva = novo_status 
        self.save() 
    

class Tipo_Combustivel(models.Model):
    nome_combustivel = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_combustivel


class Abastecimento(models.Model):
    veiculo = models.ForeignKey(Veiculo,on_delete=models.CASCADE,related_name='veiculo_abastecido')
    km_atual = models.IntegerField()
    tipo_combustivel = models.ForeignKey(Tipo_Combustivel,on_delete=models.CASCADE,related_name="combustivel_abastecimento")
    motorista = models.ForeignKey('usuarios.CustomUser',on_delete=models.CASCADE,related_name='usuario_abastecimento')
    quant_litros = models.FloatField()
    valor = models.FloatField()
    img_abastecimento = models.ImageField(
        upload_to="imagens/abastecimento",
        height_field=None,
        width_field=None,
        max_length=None
    )
    data_cadastro = models.DateField(auto_now_add=True)
    data_alteracao = models.DateField(auto_now=True)
    usuario_cadastro = models.ForeignKey(
        'usuarios.CustomUser',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="abastecimentos_cadastradas",
    )
    usuario_alteracao = models.ForeignKey(
        'usuarios.CustomUser',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="abastecimentos_alteradas",
    )

    def __str__(self):
        return f"Abatecimento {self.id} - {self.veiculo.modelo}"
    

class Tipo_Manutencao(models.Model):
    nome_manutencao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_manutencao

class Prioridade_Atendimento(models.Model):
    nome_prioridade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_prioridade


class Status_Manutencao(models.Model):
    nome_status = models.CharField(max_length=100)
    status_cor = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.nome_status

class Manutencao(models.Model):
    veiculo = models.ForeignKey(Veiculo,on_delete=models.SET_NULL,related_name='veiculo_manutencao',null=True)
    km_atual = models.IntegerField()
    tipo_manutencao = models.ForeignKey(Tipo_Manutencao,on_delete=models.SET_NULL,related_name='manutencao_tipo',null=True)
    prioridade = models.ForeignKey(Prioridade_Atendimento,on_delete=models.SET_NULL,related_name='manutencao_prioridade',null=True)
    data_prevista = models.DateField()
    valor_manutencao = models.FloatField()
    comentario = models.TextField()
    status = models.ForeignKey(Status_Manutencao,on_delete=models.SET_NULL,related_name='manutencao_status',null=True)
    data_cadastro = models.DateField(auto_now_add=True)
    data_alteracao = models.DateField(auto_now=True)
    usuario_cadastro = models.ForeignKey(
        'usuarios.CustomUser',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="manutencao_cadastrada",
    )
    usuario_alteracao = models.ForeignKey(
        'usuarios.CustomUser',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="manutencao_alterada",
    )


class Tipo_Carga(models.Model):
    descr_carga = models.CharField(max_length=100)
    
    def __str__(self):
        return self.descr_carga


class Rota(models.Model):
    data_inicio = models.DateField()
    data_fim = models.DateField()
    tipo_carga = models.ForeignKey(Tipo_Carga,on_delete=models.SET_NULL,null=True)
    cidade_inicio = models.CharField(max_length=100)
    cidade_fim = models.CharField(max_length=100)
    reserva = models.OneToOneField(Reservas,on_delete=models.CASCADE)
    data_cadastro = models.DateField(auto_now_add=True)
    data_alteracao = models.DateField(auto_now=True)
    usuario_cadastro = models.ForeignKey(
        'usuarios.CustomUser',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="rota_cadastrada",
    )
    usuario_alteracao = models.ForeignKey(
        'usuarios.CustomUser',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="rota_alterada",
    )
