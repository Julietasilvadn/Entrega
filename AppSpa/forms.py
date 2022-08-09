from django import forms
from .models import *


class UsuarioFormulario(forms.Form):
    """nombre=forms.CharField()
    apellido= forms.CharField()
    dni= forms.IntegerField()
    email= forms.EmailField()
    contraseña= forms.CharField()"""
    class Meta:
          model = Usuario
          fields = ('nombre', 'apellido', 'dni', 'email', 'contraseña')
          widgets = {
                'nombre':   forms.TextInput(attrs={'class':'form-control'}),
                'apellido':  forms.TextInput(attrs={'class': 'form-control'}),
                'dni': forms.TextInput(attrs={'class':'form-control'}),
                'email': forms.TextInput(attrs={'class':'form-control'}),
                'contraseña': forms.TextInput(attrs={'class':'form-control'}),
          }

class MascotaFormulario(forms.Form):
    nombre= forms.CharField()
    raza= forms.CharField()
    edad= forms.IntegerField()

class ReservaFormulario(forms.Form):
    dueño= forms.CharField()
    mascota= forms.CharField()
    fecha= forms.DateTimeField()