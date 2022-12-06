from pyexpat import model
from random import choices
from urllib import request
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Reserva(models.Model):
  class Estado(models.Choices):
      estado =[]
        reservado = 'RESERVADO'
        completado ='COMPLETADO'
        anulada ='ANULADA'
        noAsisten ='NO ASISTEN'
estado = models.CharField(
    max_length=25,
        choices= Estado.choices,
        default= Estado.reservado)
cliente = models.CharField(max_length=50)
fono = models.CharField(max_length=20)
fecha = models.DateField()
hora = models.TimeField()
comensales = models.IntegerField(validators=[MinValueValidator(1),
                                    MaxValueValidator(15)])

observacion = models.CharField
