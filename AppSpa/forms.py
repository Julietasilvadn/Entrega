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
    nacimiento= forms.DateField()
    imagen= forms.ImageField()

class ReservaFormulario(forms.Form):
    mascota= forms.CharField()
    dia= forms.CharField()