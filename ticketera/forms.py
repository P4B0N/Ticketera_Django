from django import forms
from django.forms import ValidationError

from .models import Ticket, Empresa, Usuario

class UsuarioForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields=['nombre_usuario','apellido_usuario','email_usuario','telefono_usuario','nombre_empresa','usuario','contrasenia_usuario']
        
    nombre_usuario=forms.CharField(
            label='Nombre', 
            widget=forms.TextInput()
        )
    
    apellido_usuario=forms.CharField(
            label='Apellido', 
            widget=forms.TextInput()
        )
    
    email_usuario=forms.CharField(
            label='Email', 
            widget=forms.TextInput()
        )
    
    telefono_usuario=forms.CharField(
            label='Teléfono', 
            widget=forms.TextInput()
        )
    
    nombre_empresa=forms.CharField(
            label='Nombre de Empresa', 
            widget=forms.TextInput()
        )
    
    usuario=forms.CharField(
            label='Nombre de usuario', 
            widget=forms.TextInput()
        )
    
    contrasenia_usuario=forms.CharField(
            label="Password",
            widget=forms.PasswordInput(),
            strip=False
        )
        
        


class TicketForm(forms.ModelForm):
    
    PRIORIDAD = (('','Seleccionar'),
                 (1,'Baja'),
                 (2,'Media'),
                 (3,'Alta'))
    
    class Meta:
        model = Ticket
        fields=['titulo', 'descripcion','prioridad','empresa']

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
            choices=PRIORIDAD,
            widget=forms.Select()
        )
    
    empresa = forms.ModelChoiceField(
        label='Empresa', 
        queryset=Empresa.objects.filter(baja=False),
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