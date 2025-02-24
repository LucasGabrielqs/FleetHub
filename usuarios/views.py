from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import re
import json
from django.db.models import Q
from datetime import datetime,date

from usuarios.models import CustomUser,StatusUsuario,TipoUsuario
from dashboard.models import Estado


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
    return render(request, 'usuarios/login.html')

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
            return render(request, 'usuarios/cadastrar.html', {
                'estados': estados,
                'error': error,
                'data': data,
            })

        # Validação do CPF: verifica se já existe um usuário com esse CPF
        if CustomUser.objects.filter(cpf=cpf).exists():
            error = "CPF já cadastrado ou inválido."
            return render(request, 'usuarios/cadastrar.html', {
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
            
            usuario.save()
            return redirect("login")
        except Exception as e:
            error = f"Erro ao cadastrar usuário: {e}"
            return render(request, 'usuarios/cadastrar.html', {
                'estados': estados,
                'error': error,
                'data': data,
            })

    # Na requisição GET, renderiza o formulário sem dados preenchidos
    return render(request, 'usuarios/cadastrar.html', {
        'estados': estados,
        'data': data,  # data pode estar vazia
    })

def recuperar_senha(request):
    return render(request, 'usuarios/recuperar-senha.html')

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
            return render(request, 'usuarios/cadastro_usuario_app.html', {
                'estados': estados,
                'error': error,
                'tipos':tipos,
                'data': data,
            })

        # Validação do CPF: verifica se já existe um usuário com esse CPF
        if CustomUser.objects.filter(cpf=cpf).exists():
            error = "CPF já cadastrado ou inválido."
            return render(request, 'usuarios/cadastro_usuario_app.html', {
                'estados': estados,
                'error': error,
                'data': data,
                'tipos':tipos
            })

        try:
            status = get_object_or_404(StatusUsuario, status="Ativo")
            tipo = get_object_or_404(TipoUsuario,nome=tipo)

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
            return redirect("listagem_usuarios")
        except Exception as e:
            error = f"Erro ao cadastrar usuário: {e}"
            return render(request, 'usuarios/cadastro_usuario_app.html', {
                'estados': estados,
                'error': error,
                'tipos':tipos,
                'data': data,
            })
    
    return render(request,'usuarios/cadastro_usuario_app.html',{
        'estados':estados,
        'tipos':tipos,
        'status':status,
        'data': data
        })

@login_required
def listagem_usuarios(request):
    query = request.GET.get('query')
    usuarios = CustomUser.objects.exclude(tipo_usuario=None)
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
    return render(request, 'usuarios/listagem_usuarios.html',{
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

    return render(request, 'usuarios/informacoes_usuarios.html', {
        'usuario': usuario,
        'estados': estados,
        'tipos': tipos_usuario,
        'status': status_usuario_list,
        'error_message': error_message,
        'success_message': success_message,
    })
