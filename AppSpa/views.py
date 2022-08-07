from django.shortcuts import render, redirect
from urllib import request
from urllib.request import Request
from django.http import HttpResponse
from datetime import date, datetime 
from AppSpa.models import Usuario, Mascota
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView


class CreateUsuario(CreateView):
    model = Usuario
    template_name = 'AppSpa/login.html'
    fields = "__all__"

    def get_success_url(self) -> str:
        return reverse_lazy('inicio')

class UpdateUsuario(UpdateView):
    model = Usuario
    succes_url = 'AppSpa/actualizar'
    fields = ['nombre', 'apellido', 'contraseña']

class DeleteUsuario(DeleteView):
    model = Usuario
    template_name = 'AppSpa/perfil.html'

class ListUsuario(ListView):
    model = Usuario
    template_name = 'AppSpa/listausuarios.html'

class DetalleUsuario(DetailView):
    model = Usuario
    template_name = 'AppSpa/perfil.html'

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
    return render(request, "AppSpa/registrarse.html")


