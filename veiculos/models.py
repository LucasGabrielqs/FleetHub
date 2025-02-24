from django.db import models
from django.apps import apps

class Status_Veiculo(models.Model):
    status = models.CharField(max_length=50, default=1)
    status_cor = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.status

class Tipo_Veiculo(models.Model):
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo

class Veiculo(models.Model):
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=100)
    valor_compra = models.FloatField()
    ano = models.IntegerField()
    km = models.IntegerField()
    tipo = models.ForeignKey(Tipo_Veiculo,on_delete=models.SET_NULL,null=True)
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
    status = models.ForeignKey(
    Status_Veiculo, 
    on_delete=models.SET_NULL,
    null=True, 
    blank=True, 
    related_name="veiculos_status"
)
    data_cadastro = models.DateField(auto_now_add=True)
    data_alteracao = models.DateField(auto_now=True)
    usuario_cadastro = models.ForeignKey(
        'usuarios.CustomUser',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="veiculos_cadastrados",
    )
    usuario_alteracao = models.ForeignKey(
        'usuarios.CustomUser',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="veiculos_alterados",
    )

    def __str__(self):
        return self.modelo

    def modificar_estados(self,value):
        novo_status = Status_Veiculo.objects.get(id=value)  
        self.status = novo_status  
        self.save() 

    def modificar_km(self,value):
        self.km = value
        self.save()