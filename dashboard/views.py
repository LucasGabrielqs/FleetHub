from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from .models import Usuario, Estado, TipoUsuario, StatusUsuario
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate
from django.contrib import messages
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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        

        usuario = Usuario.objects.get(email=username)


        print(usuario)
        if usuario is None:
            return tela_dashboard(request)
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

        

    return render(request, 'dashboard/login.html')



def cadastrar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        rua = request.POST.get('rua')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        cep = request.POST.get('cep')
        estado = request.POST.get('estado')
        senha = request.POST.get('senha')
        #imagem = request.FILES.get('img')
        estado = get_object_or_404(Estado, sigla=estado)
        tipo_usuario = get_object_or_404(TipoUsuario, id=4)#seleciona o tipo indefinido no database atual
        status_usuario = get_object_or_404(StatusUsuario, id=3)#seleciona o tipo indefinido no database atual

        usuario = Usuario.objects.create(
            nome=nome,
            email=email,
            cpf=cpf,
            telefone=telefone,
            rua=rua,
            bairro=bairro,
            cidade=cidade,
            cep=cep,
            senha=make_password(senha),
            estado=estado,
            tipo_usuario=tipo_usuario,
            status_usuario=status_usuario,
        )

    estados = get_list_or_404(Estado)
    return render(request, 'dashboard/cadastrar.html', {'estados':estados})


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
        
        usuario = get_object_or_404(Usuario, id=id)

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



    usuario = get_object_or_404(Usuario, id=1)
    estados = get_list_or_404(Estado)
    #senha=make_password(password=usuario.senha, hasher='pbkdf2_sha256')
    return render(request, 'dashboard/informacoes_usuarios.html',{'usuario':usuario, 'estados':estados})

def listagem_reservas(request):
    return render(request, 'dashboard/listagem_reservas.html')

def registro_abastecimento(request):
    return render(request, 'dashboard/registro_abastecimento.html')