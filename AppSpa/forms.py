from django import forms

class Cliente(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=30)
    dni= forms.CharField(max_length=8)
    email= forms.EmailField()
    contraseña = forms.CharField (max_length=30)
    creado = forms.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado = forms.DateTimeField(auto_now=True, verbose_name="Fecha de cambio")

class Mascota(forms.Form):
    nombre= forms.CharField(max_length=30)
    raza= forms.CharField(max_length=30)
    edad= forms.IntegerField()