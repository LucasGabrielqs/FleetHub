from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Usuário, Estado
from django.contrib.auth.hashers import make_password, check_password
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
    if request.method == 'POST':
        id = request.POST.get('id')
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        rua = request.POST.get('rua')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        cep = request.POST.get('cep')
        estado = request.POST.get('estado')
        imagem = request.FILES.get('img')
        
        usuario = get_object_or_404(Usuário, id=id)

        usuario.nome = nome
        usuario.email = email
        usuario.cpf = cpf
        usuario.telefone = telefone
        usuario.rua = rua
        usuario.bairro = bairro
        usuario.cidade = cidade
        usuario.cep = cep

        # Verifica se um arquivo foi enviado no campo "img"
        if 'img' in request.FILES:
            usuario.imagem = imagem


        usuario.estado = get_object_or_404(Estado, sigla=estado)

        usuario.save()



    usuario = get_object_or_404(Usuário, id=1)
    estados = get_list_or_404(Estado)
    #senha=make_password(password=usuario.senha, hasher='pbkdf2_sha256')
    return render(request, 'dashboard/informacoes_usuarios.html',{'usuario':usuario, 'estados':estados})

def listagem_reservas(request):
    return render(request, 'dashboard/listagem_reservas.html')

def registro_abastecimento(request):
    return render(request, 'dashboard/registro_abastecimento.html')