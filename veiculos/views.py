from email import message
import secrets
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import re
import json
from django.db.models import Q
from datetime import datetime,date


from .models import Veiculo,Tipo_Veiculo,Status_Veiculo

# Create your views here.
@login_required
def listagem_veiculos(request):
    query = request.GET.get('query')
    veiculos = Veiculo.objects.all()
    veiculos_disponiveis = Veiculo.objects.filter(status__status="Disponível").count()
    veiculos_reservados = Veiculo.objects.filter(status__status="Reservado").count()
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
    return render(request, 'veiculos/listagem_veiculos.html',{
                'veiculos':veiculos,
                'disponivel':veiculos_disponiveis,
                'reservados':veiculos_reservados,
                'emuso':veiculos_emuso,
                'atrasados':veiculos_atrasados,
                'manutencao':veiculos_manutencao
                })

@login_required
def cadastrar_veiculo(request):
    tipo_veiculo = Tipo_Veiculo.objects.all()
    status = Status_Veiculo.objects.all()
    data = {}

    if request.method == 'POST':
        print(request.POST)
        # Verificar se todos os campos obrigatórios estão presentes
        modelo = request.POST.get('modelo')
        marca = request.POST.get('marca')
        valor_compra = request.POST.get('valor')
        ano = request.POST.get('ano')
        km = request.POST.get('km')
        tipo = request.POST.get('tipo')
        motor = request.POST.get('motor')
        status_id = request.POST.get('status')
        placa = request.POST.get('placa')
        chassi = request.POST.get('chassi')
        cor = request.POST.get('cor')

        data = {
            'modelo' : modelo,
            'marca' : marca,
            'valor_compra' : valor_compra,
            'ano' : ano,
            'km' : km,
            'tipo' : tipo,
            'motor' : motor,
            'status_id' : status_id,
            'placa' : placa,
            'chassi' : chassi,
            'cor' : cor
        }



        if tipo == 'Selecione':
            messages.error(request, 'Selecione o tipo do veículo')




        
        # Certifique-se de que campos obrigatórios não estão vazios
        if modelo and marca and valor_compra and ano and km and motor and status_id and placa and chassi and cor:
            # Criar o objeto Veiculo
            print(f"Modelo: {modelo}, Marca: {marca}, Valor: {valor_compra}, status: {status_id}")
            # Buscar o objeto Status_Veiculo correspondente
            status_veiculo = Status_Veiculo.objects.get (status=status_id)
            tipo = Tipo_Veiculo.objects.get(tipo=tipo)
            print(status_veiculo)
            veiculo = Veiculo(
                modelo=modelo,
                marca=marca,
                valor_compra=valor_compra,
                ano=ano,
                km=km,
                tipo = tipo,
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
            else:
                messages.error(request,"Todos os campos devem ser preenchidos")
                return render(request, 'veiculos/cadastrar_veiculos.html',{
                'data' : data,
                'status':status,'tipo':tipo_veiculo
            })
                

            # Salvar o objeto no banco de dados
            veiculo.save()
            messages.success(request,"Veiculo salvo com sucesso")
            # Redirecionar para uma página de sucesso ou lista de veículos
            return redirect('listagem_veiculos')
        else:
            messages.error(request,'Todos os campos obrigatórios devem ser preenchidos.')
            return render(request, 'veiculos/cadastrar_veiculos.html',{
                'data' : data,
                'status':status,'tipo':tipo_veiculo
            })
        
    return render(request, 'veiculos/cadastrar_veiculos.html', {'status':status,'tipo':tipo_veiculo,'data' : data})

@login_required
def informacoes_veiculo(request, id):
    veiculo = Veiculo.objects.get(id=id)
    status_list = Status_Veiculo.objects.all()
    tipo_veiculo = Tipo_Veiculo.objects.exclude(tipo=veiculo.tipo)
    error_message = None  # Para armazenar mensagens de erro
    success_message = None  # Para indicar sucesso

    if request.method == 'POST':
        # Coleta dos dados do formulário
        modelo = request.POST.get('modelo')
        marca = request.POST.get('marca')
        valor_compra = request.POST.get('valor')
        ano = request.POST.get('ano')
        km = request.POST.get('km')
        tipo = request.POST.get('tipo')
        motor = request.POST.get('motor')
        status = request.POST.get('status')
        placa = request.POST.get('placa')
        chassi = request.POST.get('chassi')
        cor = request.POST.get('cor')
        

        if valor_compra: 
            valor_compra = valor_compra.replace(",", ".") 
            try:
                valor_compra = float(valor_compra)
            except ValueError:
                valor_compra = None 

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
            if tipo != veiculo.tipo:
                veiculo.tipo = Tipo_Veiculo.objects.get(tipo=tipo)

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

    return render(request, 'veiculos/informacoes_veiculos.html', {
        'veiculo': veiculo,
        'status': status_list,
        'error_message': error_message,
        'success_message': success_message,
        'tipo_veiculo' : tipo_veiculo
    })
