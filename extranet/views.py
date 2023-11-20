from django.shortcuts import render
from django.http import HttpResponse

def indice(request):
    return render(request, '../templates/extranet/index.html')

# Create your views here.
