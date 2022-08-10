from django import forms
from .models import *


class UsuarioFormulario(forms.Form):
    nombre=forms.CharField()
    apellido= forms.CharField()
    dni= forms.IntegerField()
    email= forms.EmailField()
    contraseña= forms.CharField()
    

class MascotaFormulario(forms.Form):
    nombre= forms.CharField()
    raza= forms.CharField()
    edad= forms.IntegerField()

class ReservaFormulario(forms.Form):
    dueño= forms.CharField()
    mascota= forms.CharField()
    fecha= forms.DateTimeField()