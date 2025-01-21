from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse

from dashboard.models import Veiculo, Status_Veiculo, Usuário, TipoUsuario, StatusUsuario, Estado
# Create your views here.



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



def listagem_veiculos(request):
    veiculos = get_list_or_404(Veiculo)
    return render(request, 'dashboard/listagem_veiculos.html',{'veiculos':veiculos})

def cadastrar_veiculo(request):
    status = get_list_or_404(Status_Veiculo)
    if request.method == 'POST':
        # Verificar se todos os campos obrigatórios estão presentes
        modelo = request.POST.get('modelo')
        marca = request.POST.get('marca')
        valor_compra = request.POST.get('valor')
        ano = request.POST.get('ano')
        km = request.POST.get('km')
        motor = request.POST.get('motor')
        status_id = request.POST.get('status')
        placa = request.POST.get('placa')
        chassi = request.POST.get('chassi')
        cor = request.POST.get('cor')
        
        # Certifique-se de que campos obrigatórios não estão vazios
        if modelo and marca and valor_compra and ano and km and motor and status_id and placa and chassi and cor:
            # Criar o objeto Veiculo
            print(f"Modelo: {modelo}, Marca: {marca}, Valor: {valor_compra}, status: {status}")
            # Buscar o objeto Status_Veiculo correspondente
            status = get_object_or_404(Status_Veiculo, status=status_id)
            veiculo = Veiculo(
                modelo=modelo,
                marca=marca,
                valor_compra=valor_compra,
                ano=ano,
                km=km,
                motor=motor,
                status=status,
                placa=placa,
                chassi=chassi,
                cor=cor,
            )

            # Verifica se um arquivo foi enviado no campo "img"
            if 'img' in request.FILES:
                veiculo.imagem = request.FILES.get('img')

            # Salvar o objeto no banco de dados
            veiculo.save()

            # Redirecionar para uma página de sucesso ou lista de veículos
            return redirect('listagem_veiculos')
        else:
            # Se algum campo obrigatório estiver faltando, retornar um erro
            return render(request, 'dashboard/cadastrar_veiculos.html', {
                'error': 'Todos os campos obrigatórios devem ser preenchidos.',
            })

    return render(request, 'dashboard/cadastrar_veiculos.html', {'status':status})


def informacoes_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    status_list = get_list_or_404(Status_Veiculo)

    if request.method == 'POST':
        # Coleta dos dados do formulário
        modelo = request.POST.get('modelo')
        marca = request.POST.get('marca')
        valor_compra = request.POST.get('valor')
        ano = request.POST.get('ano')
        km = request.POST.get('km')
        motor = request.POST.get('motor')
        status = request.POST.get('status')
        placa = request.POST.get('placa')
        chassi = request.POST.get('chassi')
        cor = request.POST.get('cor')

        # Verifica se todos os campos obrigatórios estão presentes
        if modelo and marca and valor_compra and ano and km and motor and status and placa and chassi and cor:
            veiculo.modelo = modelo
            veiculo.marca = marca
            veiculo.valor_compra = valor_compra
            veiculo.ano = ano
            veiculo.km = km
            veiculo.motor = motor
            veiculo.status = get_object_or_404(Status_Veiculo, status=status)
            veiculo.placa = placa
            veiculo.chassi = chassi
            veiculo.cor = cor

            # Verifica se um arquivo foi enviado no campo "img"
            if 'img' in request.FILES:
                veiculo.imagem = request.FILES.get('img')

            # Salvar o objeto no banco de dados
            veiculo.save()
    return render(request, 'dashboard/informacoes_veiculos.html', {'veiculo': veiculo, 'status': status_list})



def cadastro_usuario(request):
    return render(request,'dashboard/cadastro_usuario_app.html')

def listagem_usuarios(request):
    usuarios = get_list_or_404(Usuário)
    contexto = {
        'range_10': range(10),
        'range_7': range(7),  # Lista de 0 a 6
        'range_4': range(4),  # Lista de 0 a 3
        'range_2': range(2)  # Lista de 0 a 1
    }
    return render(request, 'dashboard/listagem_usuarios.html',{"contexto":contexto, 'usuarios':usuarios})


def informacoes_usuario(request, id):
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
        # Caso `estado` seja uma ForeignKey
        if hasattr(usuario, 'estado') and usuario.estado:
            estado = usuario.estado.__class__  # Obter o modelo relacionado
            usuario.estado = get_object_or_404(Estado, sigla=estado)
        else:
            usuario.estado = estado  # Caso seja um campo de texto
        usuario.save()
    usuario = get_object_or_404(Usuário, id=1)
    estados = get_list_or_404(Estado)
    tipos_usuario = get_list_or_404(TipoUsuario)
    status_usuario = get_list_or_404(StatusUsuario)
    #senha=make_password(password=usuario.senha, hasher='pbkdf2_sha256')
    return render(request, 'dashboard/informacoes_usuarios.html',{
        'usuario':usuario, 
        'estados':estados, 
        'tipos':tipos_usuario,
        'status':status_usuario,
    })



def agendar_manutencao(request):
    return render(request,'dashboard/agendar_manutencao.html')

def listagem_manutencao(request):
    contexto = {
        'range_10': range(10),
        'range_7': range(7),  # Lista de 0 a 6
        'range_4': range(4),  # Lista de 0 a 3
        'range_2': range(2)  # Lista de 0 a 1
    }
    return render(request,'dashboard/listagem_manutencao.html',contexto)

def editar_manutencao(request):
    return render(request,'dashboard/editar_manutencao.html')



def criar_reserva(request):
    return render(request, 'dashboard/criacao_reserva.html')

def editar_reserva(request):
    return render(request, 'dashboard/editar_reserva.html')

def listagem_reservas(request):
    contexto = {
        'range_10': range(10),
        'range_7': range(7),  # Lista de 0 a 6
        'range_4': range(4),  # Lista de 0 a 3
        'range_2': range(2)  # Lista de 0 a 1
    }
    return render(request, 'dashboard/listagem_reservas.html',contexto)


def criacao_rota(request):
    return render(request, 'dashboard/criacao_rota.html')

def listagem_rota(request):
    contexto = {
        'range_10': range(10),
        'range_7': range(7),  # Lista de 0 a 6
        'range_4': range(4),  # Lista de 0 a 3
        'range_2': range(2)  # Lista de 0 a 1
    }
    return render(request,'dashboard/listagem_rota.html',contexto)

def visualizacao_rota(request):
    return render(request, 'dashboard/visualizacao_rota.html')


def criacao_abastecimento(request):
    return render(request,'dashboard/criacao_abastecimento.html')

def listagem_abastecimento(request):
    contexto = {
        'range_10': range(10),
        'range_7': range(7),  # Lista de 0 a 6
        'range_4': range(4),  # Lista de 0 a 3
        'range_2': range(2)  # Lista de 0 a 1
    }
    return render(request,'dashboard/listagem_abastecimento.html',contexto)

def registro_abastecimento(request):
    return render(request, 'dashboard/registro_abastecimento.html')



def dashboard(request):
    return render(request, 'base.html')