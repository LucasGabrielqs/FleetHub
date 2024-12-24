from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dashboard(request):
    return render(request, 'base.html')

def tela_dashboard(request):
    contexto = {
        'range_10': range(10),
        'range_7': range(7),  # Lista de 0 a 6
        'range_4': range(4),  # Lista de 0 a 3
        'range_2': range(2)  # Lista de 0 a 1
    }
    return render(request, 'dashboard/dashboard.html', contexto)

def login(request):
    return render(request, 'dashboard/login.html')

def cadastrar(request):
    return render(request, 'dashboard/cadastrar.html')

def recuperar_senha(request):
    return render(request, 'dashboard/recuperar-senha.html')

def cadastro_usuario(request):
    return render(request,'dashboard/cadastro_usuario_app.html')

def agendar_manutencao(request):
    return render(request,'dashboard/agendar_manutencao.html')

def editar_manutencao(request):
    return render(request,'dashboard/editar_manutencao.html')

def criar_reserva(request):
    return render(request, 'dashboard/criacao_reserva.html')

def editar_reserva(request):
    return render(request, 'dashboard/editar_reserva.html')

def listagem_usuarios(request):
    return render(request, 'dashboard/listagem_usuarios.html')

def criacao_rota(request):
    return render(request, 'dashboard/criacao_rota.html')

def visualizacao_rota(request):
    return render(request, 'dashboard/visualizacao_rota.html')

def informacoes_usuario(request):
    return render(request, 'dashboard/informacoes_usuarios.html')

def listagem_reservas(request):
    return render(request, 'dashboard/listagem_reservas.html')

def registro_abastecimento(request):
    return render(request, 'dashboard/registro_abastecimento.html')