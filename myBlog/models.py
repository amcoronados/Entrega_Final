from django.db import models

# Create your models here.

class Carrera(models.Model):
    nombre_carrera = models.CharField(max_length = 40)
    ciudad = models.CharField(max_length = 40)
    pais = models.CharField(max_length = 20)
    distancia = models.FloatField()

class Gear(models.Model):
    tipo_gear = models.CharField(max_length = 20)
    modelo_gear = models.CharField(max_length = 60)
    marca = models.CharField(max_length = 20)
    precio = models.FloatField()

