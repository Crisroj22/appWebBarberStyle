from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Estas en el index de la app de login y registro.")

# Create your views here.
