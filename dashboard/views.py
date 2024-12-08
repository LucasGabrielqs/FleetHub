from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dashboard(request):
    return render(request, 'dashboard/sidebar-footer.html')

def login(request):
    return render(request, 'dashboard/login.html')

def cadastrar(request):
    return render(request, 'dashboard/cadastrar.html')

def recuperar_senha(request):
    return render(request, 'dashboard/recuperar-senha.html')

def cadastrar_veiculo(request):
    return render(request, 'dashboard/cadastrar_veiculos.html')

def cadastro_usuario(request):
    return render(request,'dashboard/cadastro_usuario_app.html')

def agendar_manutencao(request):
    return render(request,'dashboard/agendar_manutencao.html')

def editar_manutencao(request):
    return render(request,'dashboard/editar_manutencao.html')

def criar_reserva(request):
    return render(request, 'dashboard/criacao_reserva.html')



def home_view(request):
    return render(request, 'base.html')