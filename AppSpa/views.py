from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime 
from AppSpa.forms import Cliente, Mascota
from AppSpa.models import Usuario, Mascota

def base(request):
    return render (request, 'inicio/index.html', {})

def inscripcion (request):
    if request.method == 'POST':
        inscripcion_cliente = Cliente (request.POST)
        if inscripcion_cliente.is_valid:
            datos = inscripcion_cliente.cleaned_data
            cliente = Usuario (nombre=datos['nombre'], apellido=datos['apellido'], dni=datos['dni'], email=datos['email'], contraseña=datos["contraseña"], creado=datos['fecha de creacion'], actualizado=datos['fecha de cambio '])
            cliente.save()

            return render (request, 'index.html', {'mensaje':'Cliente ingresado con exito'})

        else:
            inscripcion_cliente = Cliente ()

        return render(request, 'index.html', {'incrispcion_cliente': inscripcion_cliente})


def animal (request):
    if request.method == 'POST':
        lista_mascota = Mascota (request.POST)
        if lista_mascota.is_valid:
                datos = lista_mascota.cleaned_data
                mascota = Mascota (nombre=datos['nombre'], raza=datos['raza'], edad=datos['edad'])         
                mascota.save()

                return render (request, 'index.html', {'mensaje':'la mascota ha sido ingresada'})
        else:
                lista_mascota = Mascota ()

        return render(request, 'index.html', {'lista_mascota': lista_mascota})

def mostrar_login(request):
    return render(request, "AppSpa/login.html")

def mostrar_inicio(request):
    return render(request, "AppSpa/inicio.html")

def mostrar_mascotas(request):
    return render(request, "AppSpa/mascotas.html")

def mostrar_perfil(request):
    return render(request, "AppSpa/perfil.html")

def mostrar_reserva(request):
    return render(request, "AppSpa/reserva.html")
