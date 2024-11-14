from django.urls import path
from .views import dashboard

urlpatterns = [
    path('',dashboard),
    #path('criar_enquete/', views.criar_enquete, name='criar_enquete')
]
