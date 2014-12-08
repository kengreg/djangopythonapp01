from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
#models es la es una serie de caracteristicas que tiene django 
#models = a una carpeta principal que hay en django
#Model = es un archivo py
#null = puede o no existir, para dar opcion
class Persona(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15,null=True,blank=True)
    edad = models.PositiveSmallIntegerField()
    sexo = models.CharField(max_length=1,choices=(('M','Hombre'),('F','Mujer')))

    