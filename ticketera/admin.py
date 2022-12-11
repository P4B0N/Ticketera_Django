from django.contrib import admin

from ticketera.models import Usuario, Empresa, Ticket

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Empresa)
admin.site.register(Ticket)