from django.urls import path
from . import views

urlpatterns = [
    #path('dashboards',views.dashboard, name='dashboard'),
    path('dashboard',views.tela_dashboard, name='tela_dashboard'),
    path('agendar_manutencao',views.agendar_manutencao,name='agendar_manutencao'),
    path('listagem_manutencao',views.listagem_manutencao,name='listagem_manutencao'),
    path('editar_manutencao/<int:id>/',views.editar_manutencao,name='editar_manutencao'),
    path('criar_reserva',views.criar_reserva,name='criar_reserva'),
    path('listagem_reservas', views.listagem_reservas, name='listagem_reservas'),
    path('editar_reserva/<int:id>/',views.editar_reserva,name='editar_reserva'),
    path('criar-rota/<int:id>/', views.criacao_rota,name='criacao_rota'),
    path("listagem_rota",views.listagem_rota,name='listagem_rota'),
    path('visualizacao_rota/<int:id>/',views.visualizacao_rota,name='visualizacao_rota'),
    path('criacao_abastecimento',views.criacao_abastecimento,name='criacao_abastecimento'),
    path('listagem_abastecimento',views.listagem_abastecimento,name='listagem_abastecimento'),
    path('registro_abastecimento/<int:id>/', views.registro_abastecimento, name='registro_abastecimento'),
    path('confirmar-entrega/<int:reserva_id>/', views.confirmar_entrega, name='confirmar_entrega'),
    # path('informacoes_veiculo', views.informacoes_veiculo, name='informacoes_veiculo'),

]
