from django.urls import path
from . import views

urlpatterns = [
    path('dashboards',views.dashboard, name='dashboard'),
    path('dashboard',views.tela_dashboard, name='tela_dashboard'),
    path('',views.login, name='login'),
    path('cadastrar',views.cadastrar,name='cadastrar'),
    path('recuperar-senha/',views.recuperar_senha, name='recuperar_senha'),
    
    path('cadastrar_usuario',views.cadastro_usuario,name='cadastrar_usuario'),
    path('agendar_manutencao',views.agendar_manutencao,name='agendar_manutencao'),
    path('editar_manutencao',views.editar_manutencao,name='editar_manutencao'),
    path('criar_reserva',views.criar_reserva,name='criar_reserva'),
    path('editar_reserva',views.editar_reserva,name='editar_reserva'),
    
    path('listagem-usuarios',views.listagem_usuarios,name='listagem_usuarios'),
    path('criacao_rota',views.criacao_rota,name='criacao_rota'),
    path('visualizacao_rota',views.visualizacao_rota,name='visualizacao_rota'),
    path('informacoes_usuario',views.informacoes_usuario,name='informacoes_usuario'),
    path('listagem_reservas', views.listagem_reservas, name='listagem_reservas'),
    path('registro_abastecimento', views.registro_abastecimento, name='registro_abastecimento'),
]
