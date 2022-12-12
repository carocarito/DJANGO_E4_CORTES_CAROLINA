from pyexpat import model
from random import choices
from urllib import request
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Reserva(models.Model):
      cliente = models.CharField(max_length=50)
      fono = models.CharField(max_length=20)
      fecha = models.DateField()
      hora = models.TimeField()
      comensales = models.IntegerField(validators=[MaxValueValidator(15), 
                                                   MinValueValidator(1)])
      observacion = models.CharField(max_length=200)
      estado = models.CharField(max_length=50)