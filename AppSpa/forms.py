from django import forms


class CrearUsuarioFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido= forms.CharField(max_length=30)
    dni= forms.CharField(max_length=8)
    email= forms.EmailField()
    contraseña= forms.CharField(max_length=30)