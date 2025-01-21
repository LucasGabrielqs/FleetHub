from django.db import models

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

    def __str__(self):
        return self.modelo