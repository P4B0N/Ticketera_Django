from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone
from datetime import timedelta

# Create your models here.

class Empresa (models.Model):
    nombre_empresa = models.CharField(max_length=50, verbose_name="Nombre de la empresa")
    direccion_empresa = models.CharField(max_length=50, verbose_name="Dirección de la empresa")
    telefono_empresa = models.CharField(max_length=50, verbose_name="Teléfono de la empresa")
    email_empresa = models.EmailField(max_length=50, verbose_name="Email de la empresa")
    baja = models.BooleanField(default=False)
      
    def __str__(self):
        return self.nombre_empresa
    
    def soft_delete(self):
        self.baja = True
        self.save()
        
    def restore(self):
        self.baja = False
        self.save()


class Usuario (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #nombre_usuario = models.CharField(max_length=50, verbose_name="Nombre")
    #apellido_usuario = models.CharField(max_length=50, verbose_name="Apellido")
    #email_usuario = models.EmailField(max_length=50, verbose_name="Email")
    telefono_usuario = models.CharField(max_length=50, verbose_name="Teléfono")
    empresa = models.ManyToManyField(Empresa, verbose_name="Empresa")
    #usuario = models.CharField(max_length=50, verbose_name="Usuario")
    #contrasenia_usuario = models.CharField(max_length=50, verbose_name="Contraseña") #(label="Password", widget=forms.PasswordInput, strip=False)
    #baja = models.BooleanField(default=False)
    es_supervisor = models.BooleanField(default=False)
    es_empleado = models.BooleanField(default=False)
      
    def __str__(self):
        return (self.user.first_name +" "+ self.user.last_name)
    """
    def soft_delete(self):
        self.baja = True
        self.save()
        
    def restore(self):
        self.baja = False
        self.save()
    """
    
class Ticket (models.Model):
    
    PRIORIDAD = ((1,'Baja'),
                 (2,'Media'),
                 (3,'Alta'))
    
    ESTADO = ((1,'Espera'), 
              (2,'En curso'),
              (3,'Resuelto'))
    
    titulo = models.CharField(max_length=50, verbose_name="Título")
    descripcion = models.CharField(max_length=300, verbose_name="Descripción")
    prioridad = models.IntegerField(choices=PRIORIDAD, verbose_name="Prioridad")
    estado = models.IntegerField(choices=ESTADO, default=1, verbose_name="Estado")
    fecha_creacion = models.DateField(verbose_name="Fecha de creación", default=timezone.now())
    fecha_cierre = models.DateField(verbose_name="Fecha de cierre", default=timezone.now()+timedelta(days=30)) 
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuario")
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name="Empresa")
    respuesta = models.CharField(max_length=300, default="", verbose_name="Respuesta")
    
    def __str__(self):
        return self.titulo