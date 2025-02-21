from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import re
from datetime import datetime

from dashboard.models import Veiculo, Status_Veiculo, CustomUser, TipoUsuario, StatusUsuario, Estado,Forma_Pagamento,Reservas,Status_Reserva,Abastecimento,Manutencao,Prioridade_Atendimento,Tipo_Combustivel,Tipo_Manutencao,Status_Manutencao



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
        print(request.POST)
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
                tipo_usuario=tipo,
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
    tipo_manutencao_list = get_list_or_404(Tipo_Manutencao)
    prioridade_list = get_list_or_404(Prioridade_Atendimento)
    veiculo_list = get_list_or_404(Veiculo)

    error = None
    data = {}

    print(request.POST)
    if request.method == 'POST':
        veiculo = request.POST.get('veiculo')
        km_atual = request.POST.get('km_atual')
        tipo_manutencao = request.POST.get('tipo_manutencao')
        prioridade = request.POST.get('prioridade')
        data_prevista = request.POST.get('data_prevista')
        valor_manutencao = request.POST.get('valor_manutencao')
        comentario = request.POST.get('comentario')

        data_prevista_obj = datetime.strptime(data_prevista, '%d/%m/%Y')  
        data_atual_obj = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
        data_formatada = datetime.strptime(data_prevista, '%d/%m/%Y').strftime('%Y-%m-%d')

        data = {
            'veiculo': veiculo,
            'km_atual': km_atual,
            'tipo_manutencao': tipo_manutencao,
            'prioridade': prioridade,
            'data_prevista': data_prevista,
            'valor_manutencao': valor_manutencao,
            'comentario': comentario
        }

        if any(value is None or value == "" for value in [veiculo, km_atual, tipo_manutencao, prioridade, data_prevista, valor_manutencao, comentario]):
            error = 'Por favor, preencha todos os campos obrigatórios'
            return render(request, 'dashboard/agendar_manutencao.html', {
                'data': data,
                'tipo_manutencao': tipo_manutencao_list,
                'prioridade': prioridade_list,
                'veiculo': veiculo_list,
                'error': error
            })
        
        if (data_prevista_obj<data_atual_obj):
            error = 'Data informada, é menor que a data atual'
            return render(request, 'dashboard/agendar_manutencao.html', {
                'data': data,
                'tipo_manutencao': tipo_manutencao_list,
                'prioridade': prioridade_list,
                'veiculo': veiculo_list,
                'error': error
            })

        try:
            veiculo_obj = Veiculo.objects.get(id=veiculo)
            tipo_manutencao_obj = Tipo_Manutencao.objects.get(id=tipo_manutencao)
            prioridade_obj = Prioridade_Atendimento.objects.get(id=prioridade)
        except Veiculo.DoesNotExist:
            error = "Veículo não encontrado."
            return render(request, 'dashboard/agendar_manutencao.html', {'error': error})
        except Tipo_Manutencao.DoesNotExist:
            error = "Tipo de manutenção não encontrado."
            return render(request, 'dashboard/agendar_manutencao.html', {'error': error})
        except Prioridade_Atendimento.DoesNotExist:
            error = "Prioridade não encontrada."
            return render(request, 'dashboard/agendar_manutencao.html', {'error': error})

        try:
            km_atual = int(km_atual)
            valor_manutencao = float(valor_manutencao)
        except ValueError:
            error = "Erro ao converter KM ou Valor da Manutenção. Verifique os valores inseridos."
            return render(request, 'dashboard/agendar_manutencao.html', {'error': error})

        veiculo_obj.modificar_estados(25)

        try:
            manutencao = Manutencao(
                veiculo=veiculo_obj,
                km_atual=km_atual,
                tipo_manutencao=tipo_manutencao_obj,
                status = Status_Manutencao.objects.get(id=2),
                prioridade=prioridade_obj,
                data_prevista=data_formatada,
                valor_manutencao=valor_manutencao,
                comentario=comentario
            )

            manutencao.usuario_cadastro = request.user if request.user.is_authenticated else 'ADMIN'
            manutencao.save()

            print(f"Manutenção cadastrada: {manutencao.id}")

            return redirect('listagem_manutencao')

        except Exception as e:
            error = f"Erro ao Registrar Manutenção: {e}"

    return render(request, 'dashboard/agendar_manutencao.html', {
        'data': data,
        'tipo_manutencao': tipo_manutencao_list,
        'prioridade': prioridade_list,
        'veiculo': veiculo_list,
        'error': error
    })


@login_required
def listagem_manutencao(request):
    manutencao = Manutencao.objects.all()
    return render(request,'dashboard/listagem_manutencao.html',{
        'manutencao' : manutencao
    })

@login_required
def editar_manutencao(request,id):
    manutencao = get_object_or_404(Manutencao,id=id)
    tipo_manutencao_list = get_list_or_404(Tipo_Manutencao)
    prioridade_list = get_list_or_404(Prioridade_Atendimento)
    veiculo_list = Veiculo.objects.exclude(status_id=23).exclude(modelo=manutencao.veiculo.modelo)
    status_manutencao_list = get_list_or_404(Status_Manutencao)
    error_message = None  # Para mensagens de erro
    success_message = None  # Para mensagens de sucesso

    if request.method == 'POST':
        veiculo_id = request.POST.get('veiculo')
        km_atual = request.POST.get('km_atual')
        tipo_manutencao_id = request.POST.get('tipo_manutencao')
        prioridade_id = request.POST.get('prioridade')
        data_prevista = request.POST.get('data_prevista')
        valor_manutencao = request.POST.get('valor_manutencao')
        comentario = request.POST.get('comentario')
        status_manutencao_id = request.POST.get('status')

        print(request.POST)
        alterado = False  # Flag para verificar se houve alguma alteração

        # Validações e atualização apenas se houver mudanças
        if veiculo_id != manutencao.veiculo.modelo:
            manutencao.veiculo = get_object_or_404(Veiculo, modelo=veiculo_id)
            alterado = True
        
        if km_atual and km_atual != str(manutencao.km_atual):
            manutencao.km_atual = km_atual
            alterado = True

        if data_prevista and data_prevista != str(manutencao.data_prevista):
            manutencao.data_prevista = data_prevista
            alterado = True

        if tipo_manutencao_id != manutencao.tipo_manutencao.nome_manutencao:
            manutencao.tipo_manutencao = get_object_or_404(Tipo_Manutencao, nome_manutencao=tipo_manutencao_id)
            alterado = True

        if prioridade_id != manutencao.prioridade.nome_prioridade:
            manutencao.prioridade = get_object_or_404(Prioridade_Atendimento, nome_prioridade=prioridade_id)
            alterado = True

        if valor_manutencao and valor_manutencao != str(manutencao.valor_manutencao):
            manutencao.valor_manutencao = valor_manutencao
            alterado = True
        
        if comentario and comentario != manutencao.comentario:
            manutencao.comentario = comentario
            alterado = True

        if status_manutencao_id != manutencao.status.nome_status:
            manutencao.status= get_object_or_404(Status_Manutencao, nome_status=status_manutencao_id)
            if status_manutencao_id == 'Realizada':
                manutencao.veiculo.modificar_estados(21)
            alterado = True

        # Apenas salva se alguma alteração foi feita
        if alterado:
            manutencao.save()
            messages.success(request, "Informações de Manutenção atualizadas com sucesso!")
        else:
            messages.info(request, "Nenhuma alteração foi feita.")

        return redirect('editar_manutencao', id=id)

    return render(request,'dashboard/editar_manutencao.html',{
            'manutencao' : manutencao,
            'tipo_manutencao_list' : tipo_manutencao_list,
            'prioridade_list' : prioridade_list,
            'veiculo_list' : veiculo_list,
            'status_list' : status_manutencao_list,
    })

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
    tipo_combustivel = get_list_or_404(Tipo_Combustivel)
    veiculo = get_list_or_404(Veiculo)
    motorista = get_list_or_404(CustomUser)
    data = {}
    error = None

    print(request.POST)

    if request.method == 'POST':
        print(f"Dados recebidos no POST: {request.POST}")
        veiculo_id = request.POST.get('veiculo')
        km_atual = request.POST.get('km_atual')
        tipo_combustivel_id = request.POST.get('tipo_combustivel')
        motorista_id = request.POST.get('motorista')
        quant_litros = request.POST.get('quant_litros')
        valor = request.POST.get('valor')
        imagem = request.FILES.get('img')


        data = {
            'veiculo' : veiculo_id,
            'km_atual' : km_atual,
            'tipo_combustivel' : tipo_combustivel_id,
            'motorista' : motorista_id,
            'quant_litros' : quant_litros,
            'valor' : valor,
        }

        if not all([veiculo_id, km_atual, tipo_combustivel_id, motorista_id, quant_litros, valor]):
                print(f"Erro: Campos obrigatórios faltando! veiculo_id={veiculo_id}, km_atual={km_atual}, tipo_combustivel_id={tipo_combustivel_id}, motorista_id={motorista_id}, quant_litros={quant_litros}, valor={valor}")  
                error = "Por favor, preencha todos os campos obrigatórios."
                return render(request, 'dashboard/criacao_abastecimento.html', {
                    'data': data,
                    'tipo_combustivel': tipo_combustivel,
                    'motorista': motorista,
                    'veiculo': veiculo,
                    'error': error,
                })

        try:
            tipo_combustivel = get_object_or_404(Tipo_Combustivel, id=tipo_combustivel_id)
            veiculo = get_object_or_404(Veiculo, id=veiculo_id)
            motorista = get_object_or_404(CustomUser, id=motorista_id)

            abastecimento = Abastecimento(
                veiculo=veiculo,
                km_atual=km_atual,
                tipo_combustivel=tipo_combustivel,
                motorista=motorista,
                quant_litros=quant_litros,
                valor=valor
            )

            if request.user.is_authenticated:
                abastecimento.usuario_cadastro = request.user
            else:
                abastecimento.usuario_cadastro = 'ADMIN'

            if imagem:
                abastecimento.img_abastecimento = imagem

            abastecimento.save()
            return redirect('listagem_abastecimento')
        
        except Exception as e:
            error = f"Erro ao Registrar Abastecimento: {e}"

    return render(request, 'dashboard/criacao_abastecimento.html', {
        'data': data,
        'veiculo': veiculo,
        'tipo_combustivel': tipo_combustivel,
        'motorista': motorista,
        'error': error,
    })

@login_required
def listagem_abastecimento(request):
    query = request.GET.get('query')
    abastecimento = Abastecimento.objects.all()
    return render(request, 'dashboard/listagem_abastecimento.html',{
                'abastecimentos':abastecimento,
                })

@login_required
def registro_abastecimento(request):
    return render(request, 'dashboard/registro_abastecimento.html')

@login_required
def dashboard(request):
    return render(request, 'base.html')