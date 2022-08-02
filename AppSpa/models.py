from django.db import models

class Usuario(models.Model):

    nombre=models.CharField(max_length=40)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()


class Mascota(models.Model):
    nombre= models.CharField(max_length=30)
    raza= models.CharField(max_length=30)
    edad= models.IntegerField()


