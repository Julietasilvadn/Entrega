from django import forms


class CrearUsuarioFormulario(forms.Form):
    nombre=forms.CharField()
    apellido= forms.CharField()
    dni= forms.CharField()
    email= forms.EmailField()
    contraseña= forms.CharField()