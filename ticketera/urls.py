from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('ticketera/bienvenida', views.bienvenida, name="bienvenida"),
    path('ticketera/confirmacion_ticket', views.confirmacion_ticket, name="confirmacion_ticket"),
    path('ticketera/envio_confirmado', views.envio_confirmado, name="envio_confirmado"),
    path('ticketera/login', views.login, name="login"),
    path('ticketera/nuevo_ticket', views.nuevo_ticket, name="nuevo_ticket"),
    path('ticketera/registro', views.registro, name="registro"),
    path('ticketera/seguimiento', views.seguimiento, name="seguimiento"),
]
