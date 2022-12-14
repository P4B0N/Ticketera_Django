from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    re_path(r'^ticketera/bienvenida/(?P<nombre>\w+)/$', views.bienvenida, name="bienvenida"),
    path('ticketera/envio_confirmado', views.envio_confirmado, name="envio_confirmado"),
    path('ticketera/login', views.login, name="login"),
    path('ticketera/nuevo_ticket', views.nuevo_ticket, name="nuevo_ticket"),
    path('ticketera/registro', views.registro, name="registro"),
    path('ticketera/seguimiento', views.seguimiento, name="seguimiento"),
    path('ticketera/ver_ticket/<int:ticket_id>', views.ver_ticket, name="ver_ticket"),
    path('ticketera/respuesta_ticket/<int:ticket_id>', views.respuesta_ticket, name="respuesta_ticket"),
    path('ticketera/respuesta_enviada', views.respuesta_enviada, name="respuesta_enviada"),
    path('ticketera/registro_empresa', views.registro_empresa, name="registro_empresa"),
    path('ticketera/logout', views.logout_view, name="logout"),
]
