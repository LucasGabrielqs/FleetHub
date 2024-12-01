from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard, name='dashboard'),
    path('login/',views.login, name='login'),
    path('recuperar-senha/',views.recuperar_senha, name='recuperar_senha'),
    #path('criar_enquete/', views.criar_enquete, name='criar_enquete')
]
