from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField

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
    
class Variostelefonos(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{7,15}$', message="Minimo 7 cifras: '+1234567'.")
    casa = models.CharField(validators=[phone_regex],max_length=15,null=True,blank=True)
    #trabajo = PhoneNumberField(blank=True)
    #celular = PhoneNumberField(blank=True)
    #fax = PhoneNumberField(blank=True)
    #otro = PhoneNumberField(blank=True)
    persona = models.ForeignKey(Persona)
    


    