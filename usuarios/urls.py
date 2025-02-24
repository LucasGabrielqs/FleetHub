from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_view, name='login'),
    path('logout/', views.logout_view, name="logout"),
    path('cadastrar',views.cadastrar,name='cadastrar'),
    path('recuperar-senha/',views.recuperar_senha, name='recuperar_senha'),
    path('cadastrar_usuario',views.cadastro_usuario,name='cadastrar_usuario'),
    path('listagem-usuarios',views.listagem_usuarios,name='listagem_usuarios'),
    path('informacoes_usuario/<int:id>/',views.informacoes_usuario,name='informacoes_usuario'),    
]
