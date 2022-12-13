from django.shortcuts import render, redirect
from django.http import HttpResponse
from ticketera.models import Ticket
from ticketera.forms import UsuarioForm, UserForm, TicketForm, EmpresaForm

from  django.contrib.auth import logout, authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.conf import settings


nombre=""  # Nombre del usuario logueado

# Create your views here.
def index(request):
    return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url=settings.LOGIN_URL)
def bienvenida(request, nombre):
    return render(request, "ticketera/bienvenida.html", {"nombre":nombre})

@login_required(login_url=settings.LOGIN_URL)
def confirmacion_ticket(request):
    return render(request, "ticketera/confirmacion_ticket.html")

@login_required(login_url=settings.LOGIN_URL)
def envio_confirmado(request):
    return render(request, "ticketera/envio_confirmado.html")

def login(request):
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = auth_login(request, user)
            return redirect('bienvenida', username)
        else:
            messages.error(request, f'Usuario o password incorrecto.')
    if not request.user.is_authenticated:
        form = AuthenticationForm()
        return render(request, "ticketera/login.html",{'form': form})
    else:
        return redirect('bienvenida', request.user)

@login_required(login_url=settings.LOGIN_URL)
def nuevo_ticket(request):
    formulario = TicketForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha creado el ticket correctamente')          
        return redirect('envio_confirmado')
    return render(request, "ticketera/nuevo_ticket.html",{"formulario":formulario})

def registro(request):
    formulario = UsuarioForm(request.POST or None,request.FILES or None)
    formulario_user = UserForm(request.POST or None,request.FILES or None)
    if formulario.is_valid() and formulario_user.is_valid():
        usuario = formulario.save(commit=False)
        
        usuario_user = formulario_user.save()
        usuario.user = usuario_user
        
        usuario.save()
        
        messages.success(request,'Se ha creado el usuario correctamente')          
        return redirect('login')
    return render(request, "ticketera/registro.html",{"formulario":formulario, "formulario_user":formulario_user})

@login_required(login_url=settings.LOGIN_URL)
def seguimiento(request):
    tickets = Ticket.objects.all()
    return render(request, "ticketera/seguimiento.html",{"tickets":tickets})

@login_required(login_url=settings.LOGIN_URL)
def respuesta_ticket(request):
    return render(request, "ticketera/respuesta_ticket.html")

@login_required(login_url=settings.LOGIN_URL)
def respuesta_enviada(request):
    return render(request, "ticketera/respuesta_enviada.html")

def registro_empresa(request):
    formulario = EmpresaForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha registrado la empresa correctamente')          
        return redirect('login')
    return render(request, "ticketera/registro_empresa.html",{"formulario":formulario})
