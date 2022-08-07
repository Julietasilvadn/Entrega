from django.contrib import admin
from django.urls import path, include
from AppSpa.views import *
from msilib.schema import AdminExecuteSequence
from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('inicio/', mostrar_inicio, name='inicio'),
    path('login/', views.CreateUsuario.as_view(), name='log_in'),
    path('list/', views.ListUsuario.as_view(), name='lista'),
    path('mascotas/', mostrar_mascotas, name='mascotas'),
    path('perfil/', mostrar_perfil, name='perfil'),
    path('reserva/', mostrar_reserva, name='reserva'),
    path('registro/', mostrar_registro, name='registro'),
    ]