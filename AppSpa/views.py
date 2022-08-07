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
from AppSpa.forms import CrearUsuarioFormulario

class UsuarioCreateView(CreateView):
    model = Usuario
    template_name = "registrarse_form.html"
    fields = "__all__"
    def get_success_url(self) -> str:
        return reverse_lazy('inicio')

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


