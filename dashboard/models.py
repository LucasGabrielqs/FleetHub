from django.db import models




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
class Usuário(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=15)
    senha = models.CharField(max_length=128)
    data_cadastro = models.DateField(auto_now=True)
    rua = models.CharField(max_length=35)
    bairro = models.CharField(max_length=35)
    cidade = models.CharField(max_length=35)
    cep = models.CharField(max_length=15)
    imagem = models.ImageField(upload_to='imagens/usuario', height_field=None, width_field=None, max_length=None, default='static/img/img_perfil.jpg')
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)
    
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.SET_DEFAULT, default='indefinido')
    status_usuario = models.ForeignKey(StatusUsuario, on_delete=models.SET_DEFAULT, default='indefinido')


    def __str__(self):
        return self.nome


# Create your models here.
class Status_Veiculo(models.Model):
    status = models.CharField(max_length=50, default="Indefinido")
    def __str__(self):
        return self.status
    
class Veiculo(models.Model):
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=100)
    valor_compra = models.CharField(max_length=25)
    ano = models.IntegerField()
    km = models.CharField(max_length=20)
    motor = models.CharField(max_length=10)
    status = models.CharField(max_length=15)
    placa = models.CharField(max_length=20)
    chassi = models.CharField(max_length=20)
    cor = models.CharField(max_length=50, default='indefinido')
    imagem = models.ImageField(upload_to='imagens/veiculos', height_field=None, width_field=None, max_length=None, default='media/carro-escondido.jpg')
    status = models.ForeignKey(Status_Veiculo, on_delete=models.CASCADE)
    # Não apagar essas informações comentadas
    #data_cadastro = models.DateField(auto_now_add=True)
    #data_alteracao = models.DateField(auto_now=True)
    #usuario_cadastro = models.ForeignKey(
        #Usuário,
        #on_delete=models.SET_NULL,
        #null=True,
        #blank=True,
        #related_name="veiculos_cadastrados"
    #)
    #usuario_alteracao = models.ForeignKey(
        #Usuário,
        #on_delete=models.SET_NULL,
        #null=True,
        #blank=True,
        #related_name="veiculos_alterados"
    #)

    def __str__(self):
        return self.modelo

class Forma_Pagamento(models.Model):
    forma_pagamento = models.CharField(max_length=30,default="Indefinido")
    def __str__(self):
        return self.forma_pagamento


class Status_Reserva(models.Model):
    status = models.CharField(max_length=50, default="Indefinido")
    def __str__(self):
        return self.status


class Reservas(models.Model):
    veiculo = models.ForeignKey(Veiculo,on_delete=models.CASCADE)
    data_reserva = models.DateField()
    data_entrega = models.DateField()
    motorista = models.ForeignKey(Usuário,on_delete=models.CASCADE)
    idade_condutor = models.IntegerField()
    valor = models.FloatField()
    forma_pagamento = models.CharField(max_length=30)
    status_reserva = models.ForeignKey(Status_Reserva,on_delete=models.CASCADE)
    data_cadastro = models.DateField(auto_now_add=True)
    data_alteracao = models.DateField(auto_now=True)
    usuario_cadastro = models.ForeignKey(
        Usuário,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="veiculos_cadastrados"
    )
    usuario_alteracao = models.ForeignKey(
        Usuário,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="veiculos_alterados"
    )

