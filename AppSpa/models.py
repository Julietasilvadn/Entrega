from django.db import models

class Usuario(models.Model):

    nombre=models.CharField(max_length=40)
    apellido= models.CharField(max_length=30)
    dni= models.IntegerField()
    email= models.EmailField()
    contraseña= models.CharField(max_length=30)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido}"

class Mascota(models.Model):
    nombre= models.CharField(max_length=30)
    nacimiento= models.DateTimeField(auto_now=True)
    imagen= models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"Nombre: {self.nombre} - Nacimiento: {self.nacimiento}"


class Reserva(models.Model):
    mascota= models.CharField(max_length=40)
    dia= models.CharField(max_length=40)

    def __str__(self):
        return f"Mascota: {self.mascota} - Dia: {self.dia}"

class Avatar(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"{self.user.nombre} tiene una imagen cargada"