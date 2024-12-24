from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar-veiculo',views.cadastrar_veiculo,name='cadastrar_veiculo'),
    path('listagem-veiculos',views.listagem_veiculos,name='listagem_veiculos'),
    path('informacoes_veiculo',views.informacoes_veiculo,name='informacoes_veiculo'),
]