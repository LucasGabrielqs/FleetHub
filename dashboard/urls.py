from django.urls import path
from . import views

urlpatterns = [
    path('dashboards',views.dashboard, name='dashboard'),
    path('',views.login, name='login'),
    path('cadastrar',views.cadastrar,name='cadastrar'),
    path('recuperar-senha/',views.recuperar_senha, name='recuperar_senha'),
    path('cadastrar-veiculo',views.cadastrar_veiculo,name='cadastrar_veiculo'),
]
