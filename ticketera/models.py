from django.db import models

# Create your models here.

class Usuario (models.Model):
    nombre_usuario = models.CharField(max_length=50)
    apellido_usuario = models.CharField(max_length=50)
    email_usuario = models.EmailField(max_length=50)
    telefono_usuario = models.CharField(max_length=50)
    nombre_empresa = models.CharField(max_length=50)
    contraseña_usuario = models.CharField(max_length=50) #(label="Password", widget=forms.PasswordInput, strip=False)     
    def __str__(self):
        return self.nombre_usuario
    
class Empresa   (models.Model):
    nombre_empresa = models.CharField(max_length=50)
    direccion_empresa = models.CharField(max_length=50)
    telefono_empresa = models.CharField(max_length=50)
    email_empresa = models.EmailField(max_length=50)
    def __str__(self):
        return self.nombre_empresa

class Ticket (models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    prioridad = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    fecha_creacion = models.DateField()
    fecha_cierre = models.DateField()    
    def __str__(self):
        return self.titulo