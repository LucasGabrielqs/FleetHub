from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse

from dashboard.models import Veiculo
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



def listagem_veiculos(request):
    veiculos = get_list_or_404(Veiculo)
    return render(request, 'dashboard/listagem_veiculos.html',{'veiculos':veiculos})



def cadastrar_veiculo(request):
    if request.method == 'POST':
        # Verificar se todos os campos obrigatórios estão presentes
        modelo = request.POST.get('modelo')
        marca = request.POST.get('marca')
        valor_compra = request.POST.get('valor')
        ano = request.POST.get('ano')
        km = request.POST.get('km')
        motor = request.POST.get('motor')
        status = "Novo" #request.POST.get('status')
        placa = request.POST.get('placa')
        chassi = request.POST.get('chassi')
        cor = request.POST.get('cor')
        
        # Certifique-se de que campos obrigatórios não estão vazios
        if modelo and marca and valor_compra and ano and km and motor and status and placa and chassi and cor:
            # Criar o objeto Veiculo
            print(f"Modelo: {modelo}, Marca: {marca}, Valor: {valor_compra}, status: {status}")
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

    return render(request, 'dashboard/cadastrar_veiculos.html')




def informacoes_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    return render(request, 'dashboard/informacoes_veiculos.html',{'veiculo':veiculo})


def cadastro_usuario(request):
    return render(request,'dashboard/cadastro_usuario_app.html')

def listagem_usuarios(request):
    contexto = {
        'range_10': range(10),
        'range_7': range(7),  # Lista de 0 a 6
        'range_4': range(4),  # Lista de 0 a 3
        'range_2': range(2)  # Lista de 0 a 1
    }
    return render(request, 'dashboard/listagem_usuarios.html',contexto)

def informacoes_usuario(request):
    return render(request, 'dashboard/informacoes_usuarios.html')



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





# Já existe a parte de veiculos, está em outro app
# def informacoes_veiculo(request): 
#     return render(request, 'dashboard/informacoes_veiculo.html')