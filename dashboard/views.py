from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import re

from dashboard.models import Veiculo, Status_Veiculo, CustomUser, TipoUsuario, StatusUsuario, Estado,Forma_Pagamento,Reservas,Status_Reserva
# Create your views here.



def login_view(request):
    print(request.POST)
    # Verifica se o usuário foi redirecionado com ?next= na URL
    if "next" in request.GET:
        messages.error(request, "Você precisa estar logado para acessar essa página!")
        # Limpar mensagens manualmente (caso necessário)
        storage = messages.get_messages(request)
        for _ in storage:  # Percorre todas as mensagens para garantir que são consumidas
            pass

    if request.method == "POST":
        username = request.POST.get("username")  # Pode ser Email ou CPF
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect("tela_dashboard")  # Redireciona para a página inicial
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    return render(request, 'dashboard/login.html')

def logout_view(request):
    logout(request)
    return redirect("login")

def cadastrar(request):
    # Lista de estados para popular o campo no formulário
    estados = Estado.objects.all()  # ou get_list_or_404(Estado) se preferir

    # Dicionário para manter os dados enviados pelo usuário e repassar ao template
    data = {}
    error = None

    if request.method == 'POST':
        nome_comp = request.POST.get('nome')
        nome = re.sub(r'\b[a-zA-Z]', lambda match: match.group().upper(), nome_comp.lower()) #Deixa a primeira letra Maiuscula
        primeiro_nome = re.search(r"^\S+", nome).group()
        ultimo_nome = re.search(r"\S+$", nome).group()
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        senha = request.POST.get('senha')
        rua = request.POST.get('rua')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        cep = request.POST.get('cep')
        sigla_estado = request.POST.get('estado')

        # Armazena os dados para repopular o formulário em caso de erro
        data = {
            'nome': nome,
            'email': email,
            'cpf': cpf,
            'telefone': telefone,
            'rua': rua,
            'bairro': bairro,
            'cidade': cidade,
            'cep': cep,
            'estado': sigla_estado,
        }

        # Validação: Todos os campos obrigatórios devem ser preenchidos
        if not all([nome, email, cpf, telefone, senha, rua, bairro, cidade, cep, sigla_estado]):
            error = "Por favor, preencha todos os campos obrigatórios."
            return render(request, 'dashboard/cadastrar.html', {
                'estados': estados,
                'error': error,
                'data': data,
            })

        # Validação do CPF: verifica se já existe um usuário com esse CPF
        if CustomUser.objects.filter(cpf=cpf).exists():
            error = "CPF já cadastrado ou inválido."
            return render(request, 'dashboard/cadastrar.html', {
                'estados': estados,
                'error': error,
                'data': data,
            })

        # Obtém o objeto Estado a partir da sigla informada
        estado_obj = get_object_or_404(Estado, sigla=sigla_estado)
        # Define os defaults para tipo e status (ajuste conforme a sua lógica)
        tipo_usuario = get_object_or_404(TipoUsuario, id=2)
        status_usuario = get_object_or_404(StatusUsuario, id=1)

        try:
            usuario = CustomUser.objects.create_user(
                nome=nome,
                email=email,
                cpf=cpf,
                password=senha,
                username=email,
                first_name = primeiro_nome,
                last_name = ultimo_nome,
                telefone=telefone,
                rua=rua,
                bairro=bairro,
                cidade=cidade,
                cep=cep,
                estado=estado_obj,
                status_usuario=status_usuario,
                tipo_usuario=tipo_usuario,
            )
            # Se o usuário que está cadastrando estiver autenticado, salva os rastreamentos
            #if request.user.is_authenticated:
                #usuario.usuario_cadastro = request.user
            # else:
            #     usuario.usuario_cadastro = 'ADMIN'
            usuario.save()
            return redirect("login")
        except Exception as e:
            error = f"Erro ao cadastrar usuário: {e}"
            return render(request, 'dashboard/cadastrar.html', {
                'estados': estados,
                'error': error,
                'data': data,
            })

    # Na requisição GET, renderiza o formulário sem dados preenchidos
    return render(request, 'dashboard/cadastrar.html', {
        'estados': estados,
        'data': data,  # data pode estar vazia
    })

def recuperar_senha(request):
    return render(request, 'dashboard/recuperar-senha.html')

@login_required
def tela_dashboard(request):
    usuarios = get_list_or_404(CustomUser)
    contexto = {
        'range_10': range(10),
        'range_7': range(7),  # Lista de 0 a 6
        'range_4': range(4),  # Lista de 0 a 3
        'range_2': range(2)  # Lista de 0 a 1
    }
    return render(request, 'dashboard/dashboard.html', {'contexto':contexto, 'usuarios':usuarios})

@login_required
def listagem_veiculos(request):
    query = request.GET.get('query')
    veiculos = Veiculo.objects.all()
    veiculos_disponiveis = Veiculo.objects.filter(status__status="Disponível").count()
    veiculos_reservados = Veiculo.objects.filter(status__status="Reservados").count()
    veiculos_emuso = Veiculo.objects.filter(status__status="Em Uso").count()
    veiculos_atrasados = Veiculo.objects.filter(status__status="Atrasados").count()
    veiculos_manutencao = Veiculo.objects.filter(status__status="Manutenção").count()
    print(veiculos_disponiveis)
    if query:
        veiculos = veiculos.filter(
            modelo__icontains=query
        ) | veiculos.filter(
            placa__icontains=query
        )
    return render(request, 'dashboard/listagem_veiculos.html',{
                'veiculos':veiculos,
                'disponivel':veiculos_disponiveis,
                'reservados':veiculos_reservados,
                'emuso':veiculos_emuso,
                'atrasados':veiculos_atrasados,
                'manutencao':veiculos_manutencao
                })

@login_required
def cadastrar_veiculo(request):
    
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
            print(f"Modelo: {modelo}, Marca: {marca}, Valor: {valor_compra}, status: {status_id}")
            # Buscar o objeto Status_Veiculo correspondente
            status_veiculo = get_object_or_404(Status_Veiculo, status=status_id)
            print(status_veiculo)
            veiculo = Veiculo(
                modelo=modelo,
                marca=marca,
                valor_compra=valor_compra,
                ano=ano,
                km=km,
                motor=motor,
                status=status_veiculo,
                placa=placa,
                chassi=chassi,
                cor=cor,
            )

            if request.user.is_authenticated:
                    veiculo.usuario_cadastro = request.user

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
        
    status = get_list_or_404(Status_Veiculo)
    return render(request, 'dashboard/cadastrar_veiculos.html', {'status':status})

@login_required
def informacoes_veiculo(request, id):
    veiculo = Veiculo.objects.get(id=id)
    status_list = Status_Veiculo.objects.all()
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
                veiculo.status = Status_Veiculo.objects.get(status=status)
            if placa != veiculo.placa:
                veiculo.placa = placa
            if chassi != veiculo.chassi:
                veiculo.chassi = chassi
            if cor != veiculo.cor:
                veiculo.cor = cor

            # Verifica se um arquivo foi enviado no campo "img"
            if 'img' in request.FILES:
                veiculo.imagem = request.FILES.get('img')

            if request.user.is_authenticated:
                    veiculo.usuario_alteracao = request.user

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

@login_required
def cadastro_usuario(request):
    status = get_list_or_404(StatusUsuario)
    tipos = get_list_or_404(TipoUsuario)
    estados = get_list_or_404(Estado)  

    error = None
    data = {}

    if request.method == 'POST':
        nome_comp = request.POST.get('nome')
        nome = re.sub(r'\b[a-zA-Z]', lambda match: match.group().upper(), nome_comp.lower()) #Deixa a primeira letra Maiuscula
        primeiro_nome = re.search(r"^\S+", nome).group()
        ultimo_nome = re.search(r"\S+$", nome).group()
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        rua = request.POST.get('rua')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        cep = request.POST.get('cep')
        estado = request.POST.get('estado')
        tipo = request.POST.get('tipo_usuario')
        #status_usuario = request.POST.get('status')
        imagem = request.FILES.get('img') 

        data = {
            'nome': nome_comp,
            'email': email,
            'cpf': cpf,
            'telefone': telefone,
            'rua': rua,
            'bairro': bairro,
            'tipo': tipo,
            'cidade': cidade,
            'cep': cep,
            'estado': estado,
        }

        if not all([nome, email, cpf, telefone, rua, bairro, cidade, cep, estado]):
            error = "Por favor, preencha todos os campos obrigatórios."
            return render(request, 'dashboard/cadastro_usuario_app.html', {
                'estados': estados,
                'error': error,
                'tipos':tipos,
                'data': data,
            })

        # Validação do CPF: verifica se já existe um usuário com esse CPF
        if CustomUser.objects.filter(cpf=cpf).exists():
            error = "CPF já cadastrado ou inválido."
            return render(request, 'dashboard/cadastro_usuario_app.html', {
                'estados': estados,
                'error': error,
                'data': data,
                'tipos':tipos
            })

        try:
            status = get_object_or_404(StatusUsuario, status="Ativo")

            usuario = CustomUser(
                nome = nome,
                first_name=primeiro_nome,
                last_name=ultimo_nome,
                email=email,
                cpf=cpf,
                telefone=telefone,
                rua=rua,
                bairro=bairro,
                cidade=cidade,
                cep=cep,
                estado=get_object_or_404(Estado, sigla=estado),
                status_usuario=status,
                tipo_usuario=tipo_user,
            )
            if 'img' in request.FILES:
                usuario.imagem = imagem

            usuario.save()
            return redirect("dashboard/listagem_usuarios.html")
        except Exception as e:
            error = f"Erro ao cadastrar usuário: {e}"
            return render(request, 'dashboard/cadastro_usuario_app.html', {
                'estados': estados,
                'error': error,
                'tipos':tipos,
                'data': data,
            })
    
    return render(request,'dashboard/cadastro_usuario_app.html',{
        'estados':estados,
        'tipos':tipos,
        'status':status,
        'data': data
        })

@login_required
def listagem_usuarios(request):
    query = request.GET.get('query')
    usuarios = CustomUser.objects.all()
    usuarios_ativos = usuarios.filter(status_usuario__status="Ativo").count()
    usuarios_inativos = usuarios.filter(status_usuario__status="Inativo").count()
    usuarios_gestores = usuarios.filter(tipo_usuario__nome="Gestor").count()
    usuarios_motoristas = usuarios.filter(tipo_usuario__nome="Motorista").count()
    if query:
        usuarios = usuarios.filter(
            nome__icontains=query
        ) | usuarios.filter(
            cpf__icontains=query
        )

        print(usuarios)
    return render(request, 'dashboard/listagem_usuarios.html',{
        'usuarios':usuarios,
        'ativos':usuarios_ativos,
        "inativos":usuarios_inativos,
        'motoristas':usuarios_motoristas,
        'gestores':usuarios_gestores
        })

@login_required
def informacoes_usuario(request, id):
    usuario = get_object_or_404(CustomUser, id=id)
    estados = get_list_or_404(Estado)
    tipos_usuario = get_list_or_404(TipoUsuario)
    status_usuario_list = get_list_or_404(StatusUsuario)
    error_message = None  # Para mensagens de erro
    success_message = None  # Para mensagens de sucesso

    if request.method == 'POST':
        # Coleta de dados do formulário
        nome_comp = request.POST.get('nome')
        nome = re.sub(r'\b[a-zA-Z]', lambda match: match.group().upper(), nome_comp.lower()) #Deixa a primeira letra Maiuscula
        primeiro_nome = re.search(r"^\S+", nome).group()
        ultimo_nome = re.search(r"\S+$", nome).group()
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
            usuario.first_name = primeiro_nome
            usuario.last_name = ultimo_nome
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

@login_required
def agendar_manutencao(request):
    return render(request,'dashboard/agendar_manutencao.html')

@login_required
def listagem_manutencao(request):
    contexto = {
        'range_10': range(10),
        'range_7': range(7),  # Lista de 0 a 6
        'range_4': range(4),  # Lista de 0 a 3
        'range_2': range(2)  # Lista de 0 a 1
    }
    return render(request,'dashboard/listagem_manutencao.html',contexto)

@login_required
def editar_manutencao(request):
    return render(request,'dashboard/editar_manutencao.html')

@login_required
def criar_reserva(request):
    status = get_list_or_404(Status_Reserva)  # Obtém todos os status disponíveis
    forma_pagamento = get_list_or_404(Forma_Pagamento) # Obtém todoas as formas de pagamento disponíveis
    veiculo = get_list_or_404(Veiculo) # Obtém todas as listas de veículos disponiveis
    usuario = get_list_or_404(CustomUser) # Obtém todas as listas de usuários disponíveis
    #reservas = get_list_or_404(Reservas) # Obtém todas as listas de Reservas
    if request.method == 'POST':
        # Obtenção de dados do formulário
        veiculo_nome = request.POST.get('veiculo')
        data_reserva = request.POST.get('data_reserva')
        data_entrega = request.POST.get('data_entrega')
        motorista_id = request.POST.get('motorista')  # ID do motorista enviado no formulário
        idade_condutor = request.POST.get('idade_condutor')
        valor = request.POST.get('valor')
        forma_pagamento_id = request.POST.get('forma_pagamento')
        
        # Verificar se todos os campos obrigatórios estão preenchidos
        if veiculo_nome and data_reserva and data_entrega and motorista_id and idade_condutor and valor and forma_pagamento_id:
            # Busca o status "Pendente" na tabela Status_Reserva
            status = get_object_or_404(Status_Reserva, nome="Pendente")  # Certifique-se que o nome é exatamente "Pendente"
            
            # Busca a forma de pagamento selecionada
            forma_pagamento = get_object_or_404(Forma_Pagamento, id=forma_pagamento_id)
            
            # Busca o veículo pelo nome
            veiculo = get_object_or_404(Veiculo, nome=veiculo_nome)
            
            # Busca o motorista pelo ID
            motorista = get_object_or_404(CustomUser, id=motorista_id)
            
            # Cria o objeto Reserva
            reserva = Reservas(
                veiculo=veiculo,
                data_reserva=data_reserva,
                data_entrega=data_entrega,
                motorista=motorista,
                idade_condutor=idade_condutor,
                valor=valor,
                forma_pagamento=forma_pagamento,
                status_reserva=status,
                #usuario_cadastro=request.user  # Define o usuário logado como responsável pelo cadastro
            )
            
            # Salvar no banco de dados
            reserva.save()
            
            # Redireciona para a página de listagem de reservas
            return redirect('listagem_reservas')
         
    return render(request, 'dashboard/criacao_reserva.html', {
        'status': status,
        'forma_pagamento': forma_pagamento,
        'veiculo': veiculo,
        'usuario': usuario,
        #'reserva' : reservas
    })

@login_required
def editar_reserva(request):
    return render(request, 'dashboard/editar_reserva.html')

@login_required
def listagem_reservas(request):
    contexto = {
        'range_10': range(10),
        'range_7': range(7),  # Lista de 0 a 6
        'range_4': range(4),  # Lista de 0 a 3
        'range_2': range(2)  # Lista de 0 a 1
    }
    return render(request, 'dashboard/listagem_reservas.html',contexto)

@login_required
def criacao_rota(request):
    return render(request, 'dashboard/criacao_rota.html')

@login_required
def listagem_rota(request):
    contexto = {
        'range_10': range(10),
        'range_7': range(7),  # Lista de 0 a 6
        'range_4': range(4),  # Lista de 0 a 3
        'range_2': range(2)  # Lista de 0 a 1
    }
    return render(request,'dashboard/listagem_rota.html',contexto)

@login_required
def visualizacao_rota(request):
    return render(request, 'dashboard/visualizacao_rota.html')

@login_required
def criacao_abastecimento(request):
    return render(request,'dashboard/criacao_abastecimento.html')

@login_required
def listagem_abastecimento(request):
    contexto = {
        'range_10': range(10),
        'range_7': range(7),  # Lista de 0 a 6
        'range_4': range(4),  # Lista de 0 a 3
        'range_2': range(2)  # Lista de 0 a 1
    }
    return render(request,'dashboard/listagem_abastecimento.html',contexto)

@login_required
def registro_abastecimento(request):
    return render(request, 'dashboard/registro_abastecimento.html')

@login_required
def dashboard(request):
    return render(request, 'base.html')