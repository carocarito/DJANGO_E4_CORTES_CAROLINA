from django.contrib import admin
from appReservas.models import Reserva
# Register your models here.

class ReservaAdmin(admin.ModelAdmin):
    list_display=['cliente', 'fono', 'fecha', 'hora', 'comensales', 'estado', 'observacion']

admin.site.register(Reserva, ReservaAdmin)