from django import forms
from django.forms import ValidationError

from .models import Ticket, Empresa, Usuario

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields=['first_name','last_name','email','username','password1','password2']
        
    first_name=forms.CharField(
            label='Nombre', 
            widget=forms.TextInput()
        )
    
    last_name=forms.CharField(
            label='Apellido', 
            widget=forms.TextInput()
        )
    
    email=forms.CharField(
            label='Email', 
            widget=forms.TextInput()
        )
    
    username=forms.CharField(
            label='Nombre de usuario', 
            widget=forms.TextInput()
        )
    
    password1=forms.CharField(
            label="Password",
            widget=forms.PasswordInput(),
            strip=False
        )

    password2=forms.CharField(
            label="Repita el password",
            widget=forms.PasswordInput(),
            strip=False
        )
  
  
class UsuarioForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields=['telefono_usuario','empresa','es_supervisor','es_empleado']
    
    telefono_usuario=forms.CharField(
            label='Teléfono', 
            widget=forms.TextInput()
        )
    
    empresa=forms.ModelMultipleChoiceField(
            label='Nombre de Empresa/s',
            queryset=Empresa.objects.filter(baja=False),
            widget=forms.CheckboxSelectMultiple()
        )
    
    es_supervisor=forms.BooleanField(
            label='Es supervisor?',
            required=False
        )
    
    es_empleado=forms.BooleanField(
            label='Es empleado?',
            required=False
        )
               

class TicketForm(forms.ModelForm):
    
    class Meta:
        model = Ticket
        fields=['titulo','descripcion','prioridad','empresa','usuario','respuesta','estado']

    titulo=forms.CharField(
            label='Título', 
            widget=forms.TextInput()
        )
    
    descripcion=forms.CharField(
            label='Descripción', 
            widget=forms.Textarea(attrs={'rows': 5})
        )
    
    prioridad=forms.ChoiceField(
            label='Prioridad',
            choices=Ticket.PRIORIDAD,
            widget=forms.Select()
        )
    
    empresa = forms.ModelChoiceField(
        label='Empresa', 
        queryset=Empresa.objects.all(),
        widget=forms.Select()
    )
    
    usuario = forms.ModelChoiceField(
        label='',
        queryset=Usuario.objects.all(),
        widget=forms.HiddenInput()
    )
    
    respuesta = forms.CharField(
        label='',
        required=False,
        widget=forms.HiddenInput()
    )
    
    estado=forms.ChoiceField(
            label='Estado',
            choices=Ticket.ESTADO,
            disabled=True,
            initial=1,
            widget=forms.Select()
    )


class EmpresaForm(forms.ModelForm):
    
    class Meta:
        model = Empresa
        fields=['nombre_empresa','direccion_empresa','telefono_empresa','email_empresa']
        
    nombre_empresa=forms.CharField(
            label='Nombre', 
            widget=forms.TextInput()
        )
    
    direccion_empresa=forms.CharField(
            label='Dirección', 
            widget=forms.TextInput()
        )
    
    telefono_empresa=forms.CharField(
            label='Teléfono', 
            widget=forms.TextInput()
        )
    
    email_empresa=forms.CharField(
            label='Email', 
            widget=forms.TextInput()
        )