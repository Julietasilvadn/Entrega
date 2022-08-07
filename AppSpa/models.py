from django.db import models

class Usuario(models.Model):

    nombre=models.CharField(max_length=40)
    apellido= models.CharField(max_length=30)
    dni= models.CharField(max_length=8)
    email= models.EmailField()
    contraseña= models.CharField(max_length=30)
    creado = models.DateTimeField(auto_now_add = True)
    actualizado = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - DNI: {self.dni} - Email: {self.email} - Contraseña: {self.contraseña} - Creado: {self.creado} - Actualizado: {self.actualizado}"

class Mascota(models.Model):
    nombre= models.CharField(max_length=30)
    raza= models.CharField(max_length=30)
    edad= models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Raza: {self.raza} - Edad: {self.edad}"


