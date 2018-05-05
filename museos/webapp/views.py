from django.shortcuts import render
from django.http import HttpResponse
from .xmlparser import getrss

from .models import Museo

# Create your views here.

def barra(request):
    return HttpResponse("Bienvenido a museos esto es la barra")

def update(request):
    Museo.objects.all().delete()
    getrss()
    return HttpResponse("Base actualizada")
