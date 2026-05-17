from django.shortcuts import render
from django.http import HttpResponse

def indexView(request):
    return HttpResponse("Página principal")

def saludoView(request, nombre):
    return render(request, "app1/saludo.html", {"nombre": nombre})
