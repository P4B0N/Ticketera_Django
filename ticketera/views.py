from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "ticketera/index.html")

def bienvenida(request, nombre):
    return render(request, "ticketera/bienvenida.html", {"nombre":nombre})

def confirmacion_ticket(request):
    return render(request, "ticketera/confirmacion_ticket.html")

def envio_confirmado(request):
    return render(request, "ticketera/envio_confirmado.html")

def login(request):
    nombre="Nombre_de_usuario"
    return render(request, "ticketera/login.html",{"nombre":nombre})

def nuevo_ticket(request):
    return render(request, "ticketera/nuevo_ticket.html")

def registro(request):
    return render(request, "ticketera/registro.html")

def seguimiento(request):
    return render(request, "ticketera/seguimiento.html")
