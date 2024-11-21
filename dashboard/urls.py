from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard),
    path('login/',views.login),
    #path('criar_enquete/', views.criar_enquete, name='criar_enquete')
]
