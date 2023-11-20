from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, '../templates/autenticacion/inicioSesion.html')

def registro(request):
    return render(request, '../templates/autenticacion/registroCliente.html')
# Create your views here.
