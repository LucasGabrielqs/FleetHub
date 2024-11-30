from django.urls import path
from . import views

urlpatterns = [
    path('dashboards',views.dashboard),
    path('',views.login),
    path('cadastrar',views.cadastrar,name='cadastrar')
    #path('criar_enquete/', views.criar_enquete, name='criar_enquete')
]
