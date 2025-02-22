from django.urls import path
from . import views

urlpatterns = [
    #path('dashboards',views.dashboard, name='dashboard'),
    path('dashboard',views.tela_dashboard, name='tela_dashboard'),
    path('',views.login_view, name='login'),
    path('logout/', views.logout_view, name="logout"),
    path('cadastrar',views.cadastrar,name='cadastrar'),
    path('recuperar-senha/',views.recuperar_senha, name='recuperar_senha'),
    path('cadastrar-veiculo',views.cadastrar_veiculo,name='cadastrar_veiculo'),
    path('listagem-veiculos',views.listagem_veiculos,name='listagem_veiculos'),
    path('informacoes_veiculo/<int:id>/',views.informacoes_veiculo,name='informacoes_veiculo'),
    path('cadastrar_usuario',views.cadastro_usuario,name='cadastrar_usuario'),
    path('listagem-usuarios',views.listagem_usuarios,name='listagem_usuarios'),
    path('informacoes_usuario/<int:id>/',views.informacoes_usuario,name='informacoes_usuario'),    
    path('agendar_manutencao',views.agendar_manutencao,name='agendar_manutencao'),
    path('listagem_manutencao',views.listagem_manutencao,name='listagem_manutencao'),
    path('editar_manutencao/<int:id>/',views.editar_manutencao,name='editar_manutencao'),
    path('criar_reserva',views.criar_reserva,name='criar_reserva'),
    path('listagem_reservas', views.listagem_reservas, name='listagem_reservas'),
    path('editar_reserva',views.editar_reserva,name='editar_reserva'),
    path('criacao_rota',views.criacao_rota,name='criacao_rota'),
    path("listagem_rota",views.listagem_rota,name='listagem_rota'),
    path('visualizacao_rota',views.visualizacao_rota,name='visualizacao_rota'),
    path('criacao_abastecimento',views.criacao_abastecimento,name='criacao_abastecimento'),
    path('listagem_abastecimento',views.listagem_abastecimento,name='listagem_abastecimento'),
    path('registro_abastecimento/<int:id>/', views.registro_abastecimento, name='registro_abastecimento'),
    # path('informacoes_veiculo', views.informacoes_veiculo, name='informacoes_veiculo'),

]
