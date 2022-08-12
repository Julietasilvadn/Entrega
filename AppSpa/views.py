from django.shortcuts import render, redirect
from urllib import request
from urllib.request import Request
from django.http import HttpResponse
from datetime import date, datetime 
from AppSpa.models import *
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from AppSpa.forms import  *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

def mostrar_login(request):
    return render(request, "AppSpa/login.html")

def mostrar_inicio(request):
    return render(request, "AppSpa/inicio.html", {})

def mostrar_mascotas(request):
    return render(request, "AppSpa/mascotas.html")

def mostrar_perfil(request):
    return render(request, "AppSpa/perfil.html")

def mostrar_reserva(request):
    return render(request, "AppSpa/reserva.html")

def mostrar_registro(request):
    return render(request, "AppSpa/registrarse_form.html")

def mostrar_about(request):
    return render(request, "AppSpa/about.html")

def registrarse_formulario(request):
    if request.method == "POST":
        miFormulario = UsuarioFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            usuario = Usuario (nombre= informacion['nombre'], apellido= informacion['apellido'], dni= informacion['dni'], email= informacion['email'], contraseña= informacion['contraseña'])
            usuario.save()
            return render(request, "AppSpa/inicio.html")
    else:
        miFormulario= UsuarioFormulario()
    return render(request, "AppSpa/registrarse_form.html", {"miFormulario":miFormulario})

def crearUsuario (request):
    if request.method == 'POST':
        formulariopersona = UsuarioFormulario(request.POST)
        print(formulariopersona)

        if formulariopersona.is_valid:
            informacion = formulariopersona.cleaned_data

            usuario = Usuario (nombre = informacion ['nombre'], apellido = informacion ['apellido'], dni = informacion ['dni'], email = informacion ['email'], contraseña = informacion ['contraseña'])

            usuario.save()

            return render (request, 'AppSpa/perfil.html')
    else:
        formulariopersona = UsuarioFormulario()

    return render (request, 'AppSpa/login.html', {'formulariopersona': formulariopersona})

def eliminarUsuario (request, usuario_nombre):
    usuario = Usuario.objects.get(nombre=usuario_nombre)
    usuario.delete()

    usuarios = Usuario.objects.all ()
    contexto = {'usuarios':usuarios}
    return render (request, 'AppSpa/listausuarios.html', contexto)

def editarUsuario (request, usuario_nombre):
    usuario = Usuario.objects.get(nombre=usuario_nombre)

    if request.method == 'POST':
        formulariopersona = UsuarioFormulario(request.POST)
        print(formulariopersona)

        if formulariopersona.is_valid:
            informacion = formulariopersona.cleaned_data

            usuario.nombre = informacion['nombre']
            usuario.apellido = informacion['apellido']
            usuario.email = informacion['email']
            usuario.contraseña = informacion['contraseña']

            usuario.save()

            return render(request, 'AppSpa/inicio.html')

    else:
        formulariopersona = UsuarioFormulario(initial={'nombre':usuario.nombre, 'apellido':usuario.apellido, 'dni':usuario.dni, 'email':usuario.email, 'contraseña':usuario.contraseña})

        return render(request,'AppSpa/perfil.html', {'formulariopersona':formulariopersona, 'usuario_nombre':usuario_nombre})


class CreateUsuario(CreateView):
    model = Usuario
    template_name = 'AppSpa/login.html'
    fields = ['nombre', 'apellido', 'dni', 'email', 'contraseña']

class UpdateUsuario(UpdateView):
    model = Usuario
    succes_url = 'AppSpa/actualizar'
    fields = ['nombre', 'apellido', 'contraseña']

class DeleteUsuario(DeleteView):
    model = Usuario
    template_name = 'AppSpa/listausuarios.html'

class ListUsuario(ListView):
    model = Usuario
    template_name = 'AppSpa/listausuarios.html'

class DetalleUsuario(DetailView):
    model = Usuario
    template_name = 'AppSpa/perfil.html'

def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render (request,'AppSpa/perfil.html', {'url':avatares[0].imagen.url})

def login_request(request):

    if request.method =="POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('contraseña')

            user = authenticate(usernarme=usuario, contraseña=contraseña)

            if user is not None:
                login (request, user)

                return render(request, 'AppSpa/inicio.html', {"Mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, 'AppSpa/inicio.html', {'mensaje':'Error, ha ingresado incorrectamente los datos'})
        else:
            return render(request, 'AppSpa/inicio.html', {'mensaje':'Error, no existe el usuario'})
    form = AuthenticationForm()

    return render(request, 'AppSpa/login.html', {'form':form})

def register(request):
    if request.method == 'POST':
        form = UsuarioFormulario(request.POST)
        if form.is_valid:
            username = form.cleaned_data['username']
            form.save()
            return render (request, 'AppSpa/inicio.html', {'mensaje':'Usuario creado'})
    else:
        form = UsuarioFormulario()

    return render(request, 'AppSpa/login.html', {'form':form})

def reserva_formulario(request):
    if request.method == "POST":
        miReserva = ReservaFormulario(request.POST)
        print(miReserva)
        if miReserva.is_valid:
            informacion = miReserva.cleaned_data
            reserva = Reserva(mascota=informacion['mascota'], dia=informacion['dia'])
            reserva.save()
            return render(request, "AppSpa/inicio.html")
    else:
        miReserva=ReservaFormulario()
    return render(request, "AppSpa/reserva.html", {"miReserva":miReserva})