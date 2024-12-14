from django.urls import path
from . import views

urlpatterns = [
    path('dashboards',views.dashboard, name='dashboard'),
    path('dashboard',views.tela_dashboard, name='tela_dashboard'),
    path('',views.login, name='login'),
    path('cadastrar',views.cadastrar,name='cadastrar'),
    path('recuperar-senha/',views.recuperar_senha, name='recuperar_senha'),
    path('cadastrar-veiculo',views.cadastrar_veiculo,name='cadastrar_veiculo'),
    path('cadastrar_usuario',views.cadastro_usuario,name='cadastrar_usuario'),
    path('agendar_manutencao',views.agendar_manutencao,name='agendar_manutencao'),
    path('editar_manutencao',views.editar_manutencao,name='editar_manutencao'),
    path('criar_reserva',views.criar_reserva,name='criar_reserva'),
    path('editar_reserva',views.editar_reserva,name='editar_reserva'),
    path('listagem-veiculos',views.listagem_veiculos,name='listagem_veiculos'),
    path('listagem-usuarios',views.listagem_usuarios,name='listagem_usuarios'),
    path('criacao_rota',views.criacao_rota,name='criacao_rota'),
    path('visualizacao_rota',views.visualizacao_rota,name='visualizacao_rota'),
]
