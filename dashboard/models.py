from django.db import models

# Create your models here.

class Veiculo(models.Model):
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=100)
    valor_compra = models.IntegerField()
    ano = models.IntegerField()
    km = models.IntegerField()
    motor = models.CharField(max_length=10)
    status = models.CharField(max_length=15)
    placa = models.CharField(max_length=20)
    chassi = models.CharField(max_length=20)
    #imagem = models.ImageField(upload_to='imagens/veeiculos', height_field=None, width_field=None, max_length=None, default='static/img/img_perfil.jpg')