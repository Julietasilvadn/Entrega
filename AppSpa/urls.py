from django.urls import path
from AppSpa.views import mostrar_inicio, mostrar_login, mostrar_mascotas, mostrar_perfil, mostrar_reserva
from msilib.schema import AdminExecuteSequence
from ssl import VERIFY_ALLOW_PROXY_CERTS
from django.contrib import admin
from django.urls import path
from AppSpa.views import base
from . import views 

urlpatterns = [
    path('inicio/', mostrar_inicio, name='inicio'),
    path('suscripcion/', views.inscripcion, name='inscripcion_cliente'),
    path('login/', mostrar_login, name='log_in'),
    path('mascotas/', mostrar_mascotas, name='mascotas'),
    path('perfil/', mostrar_perfil, name='perfil'),
    path('reserva/', mostrar_reserva, name='reserva'),
]