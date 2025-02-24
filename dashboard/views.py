from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import re
import json
from django.db.models import Q
from datetime import datetime,date

from dashboard.models import Forma_Pagamento,Reservas,Status_Reserva,Abastecimento,Manutencao,Prioridade_Atendimento,Tipo_Combustivel,Tipo_Manutencao,Status_Manutencao,Tipo_Carga,Rota
from veiculos.models import Status_Veiculo,Tipo_Veiculo,Veiculo
from usuarios.models import CustomUser,StatusUsuario,TipoUsuario


@login_required
def tela_dashboard(request):
    usuarios = CustomUser.objects.exclude(tipo_usuario_id=None)
    reserva = Reservas.objects.all()
    rotas = Rota.objects.all
    return render(request, 'dashboard/dashboard.html', {
        'usuarios':usuarios,
        'reservas' : reserva,
        'rotas' : rotas
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

        if data_prevista and data_prevista.strip(): 
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
            messages.error(request,'Por favor, preencha todos os campos obrigatórios')
            return render(request, 'dashboard/agendar_manutencao.html', {
                'data': data,
                'tipo_manutencao': tipo_manutencao_list,
                'prioridade': prioridade_list,
                'veiculo': veiculo_list,
            })
        
        if (data_prevista_obj<data_atual_obj):
            messages.error(request,'Data informada, é menor que a data atual')
            return render(request, 'dashboard/agendar_manutencao.html', {
                'data': data,
                'tipo_manutencao': tipo_manutencao_list,
                'prioridade': prioridade_list,
                'veiculo': veiculo_list,
            })

        try:
            veiculo_obj = Veiculo.objects.get(id=veiculo)
            tipo_manutencao_obj = Tipo_Manutencao.objects.get(id=tipo_manutencao)
            prioridade_obj = Prioridade_Atendimento.objects.get(id=prioridade)
        except Veiculo.DoesNotExist:
            messages.error(request,"Veículo não encontrado.")
            return render(request, 'dashboard/agendar_manutencao.html')
        except Tipo_Manutencao.DoesNotExist:
            messages.error(request,"Tipo de manutenção não encontrado.")
            return render(request, 'dashboard/agendar_manutencao.html')
        except Prioridade_Atendimento.DoesNotExist:
            messages.error(request,"Prioridade não encontrada.")
            return render(request, 'dashboard/agendar_manutencao.html')

        try:
            km_atual = int(km_atual)
            valor_manutencao = float(valor_manutencao)
        except ValueError:
            messages.error(request,"Erro ao converter KM ou Valor da Manutenção. Verifique os valores inseridos.")
            return render(request, 'dashboard/agendar_manutencao.html')

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
            messages.success(request,"Manutenção cadastrada com sucesso")
            print(f"Manutenção cadastrada: {manutencao.id}")

            return redirect('listagem_manutencao')

        except Exception as e:
            messages.error = f"Erro ao Registrar Manutenção: {e}"

    return render(request, 'dashboard/agendar_manutencao.html', {
        'data': data,
        'tipo_manutencao': tipo_manutencao_list,
        'prioridade': prioridade_list,
        'veiculo': veiculo_list,
    })


@login_required
def listagem_manutencao(request):
    query = request.GET.get('query', '').strip()
    manutencao = Manutencao.objects.all()
    print(f"Query recebida: {query}")

    if query:
        manutencao = manutencao.filter(
            Q(veiculo__placa__icontains=query)
        )
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
        alterado = False 

        if valor_manutencao: 
            valor_manutencao = valor_manutencao.replace(",", ".") 
            try:
                valor_manutencao = float(valor_manutencao)
            except ValueError:
                valor_manutencao = None 

        if veiculo_id != manutencao.veiculo.modelo:
            manutencao.veiculo = get_object_or_404(Veiculo, modelo=veiculo_id)
            alterado = True
        
        if km_atual:
            try:
                km_atual = int(km_atual)  # Converte para inteiro
            except ValueError:
                messages.error(request, "Valor inválido para KM Atual.")
                return redirect('editar_manutencao', id=id)

            if manutencao.veiculo.km < km_atual:
                manutencao.km_atual = km_atual
                manutencao.veiculo.modificar_km(km_atual)
                alterado = True
            else:
                messages.error(request, "Km Atual menor que o km atual do veículo")
                return redirect('editar_manutencao', id=id)

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
    status = get_list_or_404(Status_Reserva) 
    forma_pagamento = get_list_or_404(Forma_Pagamento) 
    veiculo = Veiculo.objects.exclude(status_id__in=[22, 23, 25])
    usuario = CustomUser.objects.exclude(status_usuario_id=2).exclude(tipo_usuario_id=2).exclude(tipo_usuario_id=None)
    data = {}

    if request.method == 'POST':

        veiculo_nome = request.POST.get('veiculo')
        data_reserva = request.POST.get('data_reserva')
        data_entrega = request.POST.get('data_entrega')
        motorista_id = request.POST.get('motorista')  
        idade_condutor = request.POST.get('idade_condutor')
        valor = request.POST.get('valor')
        forma_pagamento_id = request.POST.get('forma_pagamento')

        print(request.POST)

        data = {
            'veiculo' : veiculo_nome,
            'data_reserva' : data_reserva,
            'data_entrega' : data_entrega,
            'motorista' : motorista_id,
            'idade_condutor' : idade_condutor,
            'forma_pagamento' : forma_pagamento_id
        }
        

        if not all([veiculo_nome,data_reserva,data_entrega,motorista_id,idade_condutor,valor,forma_pagamento_id]):
            messages.error(request,"Por favor preencha todos os campos obrigatórios")
            return render(request,"dashboard/criacao_reserva.html",{
                    'data' : data,
                    'status' : status,
                    'forma_pagamento' : forma_pagamento,
                    'veiculo' : veiculo,
                    'usuario' : usuario
            })
        
        data_reserva = date.fromisoformat(data_reserva) if data_reserva else None
        data_entrega = date.fromisoformat(data_entrega) if data_entrega else None
        today = date.today()
        
        if data_reserva <= today:
            messages.error(request, "A data de reserva deve ser maior que a data atual.")
            return render(request, "dashboard/criacao_reserva.html", {
                'data': data, 'status': status, 'forma_pagamento': forma_pagamento,
                'veiculo': veiculo, 'usuario': usuario
            })

        if data_entrega <= data_reserva:
            messages.error(request, "A data de entrega deve ser maior que a data de reserva.")
            return render(request, "dashboard/criacao_reserva.html", {
                'data': data, 'status': status, 'forma_pagamento': forma_pagamento,
                'veiculo': veiculo, 'usuario': usuario
            })

        try:   
            status = get_object_or_404(Status_Reserva, status="Pendente")  
            forma_pagamento = get_object_or_404(Forma_Pagamento, forma_pagamento=forma_pagamento_id)
            veiculo = get_object_or_404(Veiculo, modelo=veiculo_nome)
            motorista = get_object_or_404(CustomUser, nome=motorista_id)
            

            reserva = Reservas(
                veiculo=veiculo,
                data_reserva=data_reserva,
                data_entrega=data_entrega,
                motorista=motorista,
                idade_condutor=idade_condutor,
                valor=valor,
                forma_pagamento=forma_pagamento,
                status_reserva=status,
            )

            if request.user.is_authenticated:
                reserva.usuario_cadastro = request.user

            veiculo.modificar_estados(22)

            reserva.save()
            messages.success(request,"Reserva Cadastrada com sucesso")
            if veiculo.tipo.id == 2:
                return redirect('listagem_reservas')
            else:
                return redirect('criacao_rota', id=reserva.id)
        except Exception as e:
            print(f"{e}")
            messages.error(request,f"Erro ao Registrar Reserva: {e}")
         
    return render(request, 'dashboard/criacao_reserva.html', {
        'status': status,
        'forma_pagamento': forma_pagamento,
        'veiculo': veiculo,
        'usuario': usuario,
        'data' : data

    })

@login_required
def editar_reserva(request,id):
    reserva = get_object_or_404(Reservas,id=id)
    forma_pagamento = Forma_Pagamento.objects.exclude(forma_pagamento=reserva.forma_pagamento)
    veiculo = Veiculo.objects.exclude(modelo=reserva.veiculo.modelo).exclude(status_id__in=[22,23,25])
    motorista = CustomUser.objects.exclude(nome=reserva.motorista.nome).exclude(status_usuario_id=2).exclude(tipo_usuario_id__in =[2,None])
    status = Status_Reserva.objects.exclude(status=reserva.status_reserva.status)

    alterado = False

    if request.method == 'POST':
        veiculo_nome = request.POST.get('veiculo_nome')
        data_reserva = request.POST.get('data_reserva')
        data_entrega = request.POST.get('data_entrega')
        motorista_id = request.POST.get('motorista')  
        idade_condutor = request.POST.get('idade-condutor')
        valor = request.POST.get('valor')
        forma_pagamento_id = request.POST.get('forma_pagamento')
        status_reserva = request.POST.get('status')

        print(request.POST)

        if valor: 
            valor = valor.replace(",", ".") 
            try:
                valor = float(valor)
            except ValueError:
                valor = None 

        if veiculo_nome != reserva.veiculo.modelo:
            reserva.veiculo.modificar_estados(21)
            reserva.veiculo = get_object_or_404(Veiculo,modelo=veiculo_nome)
            reserva.veiculo.modificar_estados(22)
            alterado = True

        data_reserva = date.fromisoformat(data_reserva) if data_reserva else None
        data_entrega = date.fromisoformat(data_entrega) if data_entrega else None
        today = date.today()
    
        if data_reserva != reserva.data_reserva:
            if data_reserva <= today:
                messages.error(request, "A data de reserva deve ser maior que a data atual.")
                return redirect("editar_reserva",id=id) 
            else:
                reserva.data_reserva = data_reserva
                alterado = True

        if data_entrega != reserva.data_entrega:
            if data_entrega <= reserva.data_reserva:
                messages.error(request, "A data de entrega deve ser maior que a data de reserva.")
                return redirect("editar_reserva",id=id)
            else:
                reserva.data_entrega = data_entrega
                alterado = True

        if motorista_id != reserva.motorista.nome:
            reserva.motorista = get_object_or_404(CustomUser,nome=motorista_id)
            alterado = True

        idade_condutor = int(idade_condutor)

        if idade_condutor != reserva.idade_condutor:
            if idade_condutor>=18:
                reserva.idade_condutor = idade_condutor
                alterado = True
            else:
                messages.error(request,"Idade Minima é 18 anos")
                return redirect("editar_reserva",id=id) 

        if valor != reserva.valor:
            reserva.valor = valor
            alterado = True

        if forma_pagamento_id != reserva.forma_pagamento:
            reserva.forma_pagamento = forma_pagamento_id
            alterado = True

        if status_reserva != reserva.status_reserva.status:
            if status_reserva == "Em Andamento":
                reserva.status_reserva = get_object_or_404(Status_Reserva,status=status_reserva)
                reserva.veiculo.modificar_estados(23)
            elif status_reserva == "Concluida":
                reserva.status_reserva = get_object_or_404(Status_Reserva,status=status_reserva)
                reserva.veiculo.modificar_estados(21)
            elif status_reserva == "Cancelada":
                reserva.status_reserva = get_object_or_404(Status_Reserva,status=status_reserva)
                reserva.veiculo.modificar_estados(21)
            elif status_reserva == "Pendente":
                reserva.status_reserva = get_object_or_404(Status_Reserva,status=status_reserva)
                reserva.veiculo.modificar_estados(22)
                alterado = True

        if request.user.is_authenticated:
            reserva.usuario_alteracao = request.user

        reserva.save()
        messages.success(request,"Informações alteradas com sucesso")
        return redirect("editar_reserva",id=id)

    return render(request, 'dashboard/editar_reserva.html',{
        'forma_pagamento' : forma_pagamento,
        'motorista' : motorista,
        'status' : status,
        'veiculo' : veiculo,
        'reserva' : reserva
    })

@login_required
def listagem_reservas(request):
    querry = request.GET.get('query','').strip()
    reserva = Reservas.objects.all()

    if querry:
        reserva = reserva.filter(
            Q(veiculo__modelo__icontains=querry) | Q(motorista__nome__icontains=querry)
        )

    return render(request, 'dashboard/listagem_reservas.html',{
        'reserva' : reserva
    })

@login_required
def confirmar_entrega(request, reserva_id):
    if request.method == "POST":
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            # Imprima o corpo da requisição para ver o que está sendo enviado
            data = json.loads(request.body)
            print("Dados recebidos:", data)  # Verifique o conteúdo

            # Verifique se a ação foi "confirmar_entrega"
            if data.get('acao') == 'confirmar_entrega':
                reserva = get_object_or_404(Reservas, id=reserva_id)
            
                reserva.modificar_reserva(5)

                reserva.veiculo.modificar_estados(23)

                reserva.save()

                return JsonResponse({'success': True})

            return JsonResponse({'success': False, 'error': 'Requisição inválida'})

@login_required
def criacao_rota(request, id): 
    tipo_carga = Tipo_Carga.objects.all()  
    reserva = get_object_or_404(Reservas, id=id) 
    data = {}

    if request.method == 'POST':
        data_inicio = request.POST.get('data_inicio')
        data_fim = request.POST.get('data_fim')
        tipo_carga_id = request.POST.get('tipo_carga')
        cidade_inicio = request.POST.get('cidade_inicio')
        cidade_fim = request.POST.get('cidade_fim')

        data = {
            'data_inicio' : data_inicio,
            'data_fim' : data_fim,
            'tipo_carga' : tipo_carga_id,
            'cidade_inicio' : cidade_inicio,
            'cidade_fim' : cidade_fim
        }

        print(request.POST)

        if not all([data_inicio, data_fim, tipo_carga_id, cidade_inicio, cidade_fim]):
            messages.error(request, "Por favor, preencha todas as informações.")
            return render(request, 'dashboard/criacao_rota.html', {
                'tipos': tipo_carga,
                'reserva': reserva,
                'data': data  # Mantendo os dados preenchidos
            })

        if data_inicio < str(reserva.data_reserva):
            messages.error(request, "Data de Início menor que a data da reserva")
            return render(request, 'dashboard/criacao_rota.html', {
                'tipos': tipo_carga,
                'reserva': reserva,
                'data': data
            })
        elif data_inicio > str(reserva.data_entrega):
            messages.error(request, "Data de Início maior que a data de entrega")
            return render(request, 'dashboard/criacao_rota.html', {
                'tipos': tipo_carga,
                'reserva': reserva,
                'data': data
            })

        if data_fim < str(reserva.data_reserva):
            messages.error(request, "Data de Fim menor que a data de reserva")
            return render(request, 'dashboard/criacao_rota.html', {
                'tipos': tipo_carga,
                'reserva': reserva,
                'data': data
            })
        elif data_fim > str(reserva.data_entrega):
            messages.error(request, "Data de Fim maior que a data de entrega")
            return render(request, 'dashboard/criacao_rota.html', {
                'tipos': tipo_carga,
                'reserva': reserva,
                'data': data
            })
        elif data_fim < data_inicio:
            messages.error(request, "Data de Fim menor que a data de início")
            return render(request, 'dashboard/criacao_rota.html', {
                'tipos': tipo_carga,
                'reserva': reserva,
                'data': data
            })

        try:
            tipo_carga_obj = get_object_or_404(Tipo_Carga, descr_carga=tipo_carga_id)  # Obtém o objeto Tipo_Carga

            rota = Rota(
                reserva=reserva,
                data_inicio=data_inicio,
                data_fim=data_fim,
                tipo_carga=tipo_carga_obj,
                cidade_inicio=cidade_inicio,
                cidade_fim=cidade_fim
            )


            if request.user.is_authenticated:
                rota.usuario_cadastro = request.user

            rota.save() 


            return redirect('listagem_rota')

        except Exception as e:
            messages.error(request, f"Erro ao Registrar Rota: {e}")
            return render(request, 'dashboard/criacao_rota.html', {
                'tipos': tipo_carga,
                'reserva': reserva,
                'data': data
            })

    return render(request, 'dashboard/criacao_rota.html', {
        'tipos': tipo_carga,
        'reserva': reserva,
        'data' : data
    })

@login_required
def listagem_rota(request):
    querry = request.GET.get('query','').strip()
    rotas = Rota.objects.all()

    if querry:
        rotas = rotas.filter(
            Q(reserva__veiculo__modelo__icontains=querry) | Q(reserva__motorista__nome__icontains=querry)
        )

    return render(request,'dashboard/listagem_rota.html',{
        'rotas' : rotas
    })
    
@login_required
def visualizacao_rota(request,id):
    rotas = get_object_or_404(Rota,id=id)
    tipo_carga = Tipo_Carga.objects.exclude(descr_carga=rotas.tipo_carga.descr_carga)
    alterado = False

    if request.method == 'POST':
        data_inicio = request.POST.get('data_inicio')
        data_fim = request.POST.get('data_fim')
        tipo_carga_id = request.POST.get('tipo_carga')
        cidade_inicio = request.POST.get('cidade_rota')
        cidade_fim = request.POST.get('cidade_fim')

        if data_inicio != rotas.data_inicio:
            if data_inicio < str(rotas.reserva.data_reserva):
                messages.error(request, "Data de Início menor que a data da reserva")
                return redirect("visualizacao_rota",id=id)
            elif data_inicio > str(rotas.reserva.data_entrega):
                messages.error(request, "Data de Início maior que a data de entrega")
                return redirect("visualizacao_rota",id=id)
            else:
                rotas.data_inicio = data_inicio
                alterado = True

        if data_fim != rotas.data_fim:
            if data_fim < str(rotas.reserva.data_reserva):
                messages.error(request, "Data de Fim menor que a data de reserva")
                return redirect("visualizacao_rota",id=id)
            elif data_fim > str(rotas.reserva.data_entrega):
                messages.error(request, "Data de Fim maior que a data de entrega")
                return redirect("visualizacao_rota",id=id)
            elif data_fim < data_inicio:
                messages.error(request, "Data de Fim menor que a data de início")
                return redirect("visualizacao_rota",id=id)
            else:
                rotas.data_fim = data_fim
                alterado = True

        if tipo_carga_id != rotas.tipo_carga.descr_carga:
            rotas.tipo_carga = get_object_or_404(Tipo_Carga,descr_carga=tipo_carga_id)
            alterado = True
        
        if cidade_inicio != rotas.cidade_inicio:
            rotas.cidade_inicio = cidade_inicio
            alterado = True

        if cidade_fim != rotas.cidade_fim:
            rotas.cidade_fim = cidade_fim
            alterado = True

        if request.user.is_authenticated:
            rotas.usuario_alteracao = request.user

        rotas.save()
        messages.success(request,"Informações alteradas com sucesso")
        return redirect("visualizacao_rota",id=id)

    return render(request, 'dashboard/visualizacao_rota.html',{
        'rota' : rotas,
        'tipo_carga' : tipo_carga
    })

@login_required
def criacao_abastecimento(request):
    tipo_combustivel = get_list_or_404(Tipo_Combustivel)
    veiculo = get_list_or_404(Veiculo)
    motorista = get_list_or_404(CustomUser)
    data = {}
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
                #messages.error(request,f"Erro: Campos obrigatórios faltando! veiculo_id={veiculo_id}, km_atual={km_atual}, tipo_combustivel_id={tipo_combustivel_id}, motorista_id={motorista_id}, quant_litros={quant_litros}, valor={valor}")  
                messages.error(request,"Por favor, preencha todos os campos obrigatórios.")
                return render(request, 'dashboard/criacao_abastecimento.html', {
                    'data': data,
                    'tipo_combustivel': tipo_combustivel,
                    'motorista': motorista,
                    'veiculo': veiculo,
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

            messages.success(request,"Abastecimento Cadastrado com sucesso")
            return redirect('listagem_abastecimento')
        
        except Exception as e:
            messages.error(request,f"Erro ao Registrar Abastecimento: {e}")

    return render(request, 'dashboard/criacao_abastecimento.html', {
        'data': data,
        'veiculo': veiculo,
        'tipo_combustivel': tipo_combustivel,
        'motorista': motorista,
    })

@login_required
def listagem_abastecimento(request):
    query = request.GET.get('query', '').strip()
    abastecimento = Abastecimento.objects.all()
    print(f"Query recebida: {query}")

    if query:
        abastecimento = abastecimento.filter(
            Q(veiculo__modelo__icontains=query) | Q(motorista__nome__icontains=query)
        )

    return render(request, 'dashboard/listagem_abastecimento.html',{
                'abastecimentos':abastecimento,
                })

@login_required
def registro_abastecimento(request,id):
    abastecimento = get_object_or_404(Abastecimento,id=id)
    combustivel = Tipo_Combustivel.objects.exclude(nome_combustivel=abastecimento.tipo_combustivel.nome_combustivel)
    veiculo = Veiculo.objects.exclude(modelo=abastecimento.veiculo.modelo)
    motorista = CustomUser.objects.exclude(status_usuario_id=2).exclude(nome=abastecimento.motorista.nome)

    if request.method == 'POST':
        veiculo_id = request.POST.get('veiculo')
        km_atual = request.POST.get('km_atual')
        tipo_combustivel_id = request.POST.get('tipo_combustivel')
        motorista_id = request.POST.get('motorista')
        quant_litros = request.POST.get('quant_litros')
        valor = request.POST.get('valor')
        imagem = request.FILES.get('img')


        alterado = False

        if quant_litros:  
            quant_litros = quant_litros.replace(",", ".") 
            try:
                quant_litros = float(quant_litros)  
            except ValueError:
                quant_litros = None
            
        if valor: 
            valor = valor.replace(",", ".") 
            try:
                valor = float(valor)
            except ValueError:
                valor = None 


        if veiculo_id != abastecimento.veiculo.modelo:
            abastecimento.veiculo = get_object_or_404(Veiculo,modelo=veiculo_id)
            alterado = True
        
        if km_atual and km_atual != str(abastecimento.km_atual):
            abastecimento.km_atual = km_atual
            alterado = True

        if tipo_combustivel_id != abastecimento.tipo_combustivel.nome_combustivel:
            abastecimento.tipo_combustivel = get_object_or_404(Tipo_Combustivel,nome_combustivel=tipo_combustivel_id)
            alterado = True

        if motorista_id != abastecimento.motorista.nome:
            abastecimento.motorista.nome = get_object_or_404(CustomUser,nome=motorista_id)
            alterado = True

        if quant_litros and quant_litros != str(abastecimento.quant_litros):
            abastecimento.quant_litros = quant_litros
            alterado = True

        if valor and valor != str(abastecimento.valor):
            abastecimento.valor = valor
            alterado = True

        if 'img' in request.FILES:
                abastecimento.img_abastecimento = request.FILES.get('img')

        if request.user.is_authenticated:
            abastecimento.usuario_alteracao = request.user

        if alterado:
            abastecimento.save()
            messages.success(request,"Abastecimento alterado com sucesso!")
        else:
            messages.info(request,"Nenhuma alteração foi feita")

        return redirect('registro_abastecimento',id=id)




    return render(request, 'dashboard/registro_abastecimento.html',{
        'abastecimento' : abastecimento,
        'veiculo_list' : veiculo,
        'motorista_list' : motorista,
        'tipo_combustivel_list' : combustivel,
    })

@login_required
def dashboard(request):
    return render(request, 'base.html')