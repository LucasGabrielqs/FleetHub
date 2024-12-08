from django.urls import path
from . import views

urlpatterns = [
    path('dashboards',views.dashboard, name='dashboard'),
    path('',views.login, name='login'),
    path('cadastrar',views.cadastrar,name='cadastrar'),
    path('recuperar-senha/',views.recuperar_senha, name='recuperar_senha'),
    path('cadastrar-veiculo',views.cadastrar_veiculo,name='cadastrar_veiculo'),
    path('cadastrar_usuario',views.cadastro_usuario,name='cadastrar_usuario'),
    path('agendar_manutencao',views.agendar_manutencao,name='agendar_manutencao'),
    path('editar_manutencao',views.editar_manutencao,name='editar_manutencao'),
    path('criar_reserva',views.criar_reserva,name='criar_reserva'),
]
