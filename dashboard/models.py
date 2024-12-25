from django.db import models

# Create your models here.

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

    imagem = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None, default='static/img/img_perfil.jpg')

    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)
    
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    status_usuario = models.ForeignKey(StatusUsuario, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome