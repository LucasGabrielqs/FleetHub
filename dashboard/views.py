from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages

from dashboard.models import Veiculo, Status_Veiculo, Usuário, TipoUsuario, StatusUsuario, Estado
# Create your views here.



def tela_dashboard(request):
    usuarios = get_list_or_404(Usuário)
    contexto = {
        'range_10': range(10),
        'range_7': range(7),  # Lista de 0 a 6
        'range_4': range(4),  # Lista de 0 a 3
        'range_2': range(2)  # Lista de 0 a 1
    }
    return render(request, 'dashboard/dashboard.html', {'contexto':contexto, 'usuarios':usuarios})



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
    error_message = None  # Para armazenar mensagens de erro
    success_message = None  # Para indicar sucesso

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


        try:
            # Atualização apenas dos campos modificados
            if modelo != veiculo.modelo:
                veiculo.modelo = modelo
            if marca != veiculo.marca:
                veiculo.marca = marca
            if valor_compra != veiculo.valor_compra:
                veiculo.valor_compra = valor_compra
            if ano != veiculo.ano:
                veiculo.ano = ano
            if km != veiculo.km:
                veiculo.km = km
            if motor != veiculo.motor:
                veiculo.motor = motor
            if status != veiculo.status.status:  # Comparação pelo valor textual
                veiculo.status = get_object_or_404(Status_Veiculo, status=status)
            if placa != veiculo.placa:
                veiculo.placa = placa
            if chassi != veiculo.chassi:
                veiculo.chassi = chassi
            if cor != veiculo.cor:
                veiculo.cor = cor

            # Verifica se um arquivo foi enviado no campo "img"
            if 'img' in request.FILES:
                veiculo.imagem = request.FILES.get('img')

            # Salva as alterações
            veiculo.save()
            messages.success(request, "Dados do veículo alterados com sucesso!")
            # Redireciona para evitar que a mensagem reapareça ao recarregar a página
            return redirect('informacoes_veiculo', id=id)
        except Status_Veiculo.DoesNotExist:
            error_message = "O status selecionado é inválido."

    return render(request, 'dashboard/informacoes_veiculos.html', {
        'veiculo': veiculo,
        'status': status_list,
        'error_message': error_message,
        'success_message': success_message,
    })




def cadastro_usuario(request):
    status = get_list_or_404(StatusUsuario)
    tipos = get_list_or_404(TipoUsuario)
    estados = get_list_or_404(Estado)  

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
        tipo = request.POST.get('tipo_usuario')
        status_usuario = request.POST.get('status')
        imagem = request.FILES.get('img') 


        if nome and email and cpf and telefone and rua and bairro and cidade and cep and estado:
            usuario = Usuário(
                nome = nome,
                email=email,
                cpf=cpf,
                telefone=telefone,
                rua=rua,
                bairro=bairro,
                cidade=cidade,
                cep=cep,
                estado=get_object_or_404(Estado, sigla=estado),
                status_usuario=get_object_or_404(StatusUsuario,status=status_usuario),
                tipo_usuario=get_object_or_404(TipoUsuario,nome=tipo),
            )
            if 'img' in request.FILES:
                usuario.imagem = imagem

            usuario.save()

    return render(request,'dashboard/cadastro_usuario_app.html',{
        'estados':estados,
        'tipos':tipos,
        'status':status,
        })

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
    usuario = get_object_or_404(Usuário, id=id)
    estados = get_list_or_404(Estado)
    tipos_usuario = get_list_or_404(TipoUsuario)
    status_usuario_list = get_list_or_404(StatusUsuario)
    error_message = None  # Para mensagens de erro
    success_message = None  # Para mensagens de sucesso

    if request.method == 'POST':
        # Coleta de dados do formulário
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        rua = request.POST.get('rua')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        cep = request.POST.get('cep')
        estado_sigla = request.POST.get('estado')
        status_usuario_status = request.POST.get('status')
        tipo_usuario_status = request.POST.get('tipo_usuario')



        # Atualiza apenas os campos alterados
        if nome != usuario.nome:
            usuario.nome = nome
        if email != usuario.email:
            usuario.email = email
        if cpf != usuario.cpf:
            usuario.cpf = cpf
        if telefone != usuario.telefone:
            usuario.telefone = telefone
        if rua != usuario.rua:
            usuario.rua = rua
        if bairro != usuario.bairro:
            usuario.bairro = bairro
        if cidade != usuario.cidade:
            usuario.cidade = cidade
        if cep != usuario.cep:
            usuario.cep = cep

        print(request.POST)

        # Atualiza a ForeignKey `estado` se alterada
        estado = get_object_or_404(Estado, sigla=estado_sigla)
        if estado != usuario.estado:
            usuario.estado = estado

        # Atualiza a ForeignKey `status_usuario` se alterada
        status_usuario = get_object_or_404(StatusUsuario, status=status_usuario_status)
        if status_usuario != usuario.status_usuario:
            usuario.status_usuario = status_usuario

        # Atualiza a ForeignKey `tipo_usuario` se alterada
        tipo_usuario = get_object_or_404(TipoUsuario, nome=tipo_usuario_status)
        if tipo_usuario != usuario.tipo_usuario:
            usuario.tipo_usuario = tipo_usuario

        # Atualiza a imagem se enviada
        if 'img' in request.FILES:
            usuario.imagem = request.FILES.get('img')

        # Salva as alterações
        usuario.save()
        messages.success(request, "Informações do usuário atualizadas com sucesso!")
            # Redireciona para evitar que a mensagem reapareça ao recarregar a página
        return redirect('informacoes_usuario', id=id)

    return render(request, 'dashboard/informacoes_usuarios.html', {
        'usuario': usuario,
        'estados': estados,
        'tipos': tipos_usuario,
        'status': status_usuario_list,
        'error_message': error_message,
        'success_message': success_message,
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