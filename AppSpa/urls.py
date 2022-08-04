from django.contrib import admin
from django.urls import path, include
from AppSpa.views import *
from msilib.schema import AdminExecuteSequence

from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('inicio/', mostrar_inicio, name='inicio'),
    path('login/', mostrar_login, name='log_in'),
    path('mascotas/', mostrar_mascotas, name='mascotas'),
    path('perfil/', mostrar_perfil, name='perfil'),
    path('reserva/', mostrar_reserva, name='reserva'),
]