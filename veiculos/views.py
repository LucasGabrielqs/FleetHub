from django.shortcuts import render

# Create your views here.
def listagem_veiculos(request):
    return render(request, 'veiculos/listagem_veiculos.html')

def cadastrar_veiculo(request):
    return render(request, 'veiculos/cadastrar_veiculos.html')

def informacoes_veiculo(request):
    return render(request, 'veiculos/informacoes_veiculos.html')