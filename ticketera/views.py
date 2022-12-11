from django.shortcuts import render, redirect
from django.http import HttpResponse
from ticketera.models import Ticket
from ticketera.forms import UsuarioForm, TicketForm

from django.contrib import messages


nombre="nombre_de_usuario"  # Nombre del usuario logueado

# Create your views here.
def index(request):
    return redirect('login')

def bienvenida(request, nombre):
    return render(request, "ticketera/bienvenida.html", {"nombre":nombre})

def confirmacion_ticket(request):
    return render(request, "ticketera/confirmacion_ticket.html")

def envio_confirmado(request):
    return render(request, "ticketera/envio_confirmado.html",{"nombre":nombre})

def login(request):
    
    return render(request, "ticketera/login.html",{"nombre":nombre})

def nuevo_ticket(request):
    formulario = TicketForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha creado el ticket correctamente')          
        return redirect('envio_confirmado')
    return render(request, "ticketera/nuevo_ticket.html",{"nombre":nombre, "formulario":formulario})

def registro(request):
    formulario = UsuarioForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha creado el usuario correctamente')          
        return redirect('login')
    return render(request, "ticketera/registro.html",{"formulario":formulario})

def seguimiento(request):
    tickets = Ticket.objects.all()
    return render(request, "ticketera/seguimiento.html",{"nombre":nombre, "tickets":tickets})

def respuesta_ticket(request):
    return render(request, "ticketera/respuesta_ticket.html",{"nombre":nombre})

def respuesta_enviada(request):
    return render(request, "ticketera/respuesta_enviada.html",{"nombre":nombre})