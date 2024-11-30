from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dashboard(request):
    return render(request, 'dashboard/sidebar-footer.html')

def login(request):
    return render(request, 'dashboard/login.html')

def cadastrar(request):
    return render(request, 'dashboard/cadastrar.html')