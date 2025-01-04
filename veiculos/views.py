from django.shortcuts import render

# Create your views here.
def listagem_veiculos(request):
    contexto = {
        'range_10': range(10),
        'range_7': range(7),  # Lista de 0 a 6
        'range_4': range(4),  # Lista de 0 a 3
        'range_2': range(2)  # Lista de 0 a 1
    }
    return render(request, 'veiculos/listagem_veiculos.html',contexto)

def cadastrar_veiculo(request):
    return render(request, 'veiculos/cadastrar_veiculos.html')

def informacoes_veiculo(request):
    return render(request, 'veiculos/informacoes_veiculos.html')