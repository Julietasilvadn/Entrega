from django.db import models

class Usuario(models.Model):

    nombre=models.CharField(max_length=40)
    apellido= models.CharField(max_length=30)
    dni= models.IntegerField(max_length=8)
    email= models.EmailField()
    contraseña= models.CharField(max_length=30)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - DNI: {self.dni} - Email: {self.email} - Contraseña: {self.contraseña} - Creado: {self.creado} - Actualizado: {self.actualizado}"

class Mascota(models.Model):
    nombre= models.CharField(max_length=30)
    raza= models.CharField(max_length=30)
    edad= models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Raza: {self.raza} - Edad: {self.edad}"


class Reserva(models.Model):
    dueño= models.CharField(max_length=40)
    mascota= models.CharField(max_length=40)
    fecha= models.DateTimeField()

    def __str__(self):
        return f"Dueño: {self.dueño} - Mascota: {self.mascota} - Fecha: {self.fecha}"

class Avatar(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to='avatares', null=True, blank=True)
