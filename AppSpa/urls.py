from django.urls import path
from AppSpa.views import mostrar_inicio, mostrar_login, mostrar_mascotas, mostrar_perfil, mostrar_reserva


urlpatterns = [
    path('inicio/', mostrar_inicio, name="inicio"),
    path('login/', mostrar_login, name="log-in"),
    path('mascotas/', mostrar_mascotas, name="mascotas"),
    path('perfil/', mostrar_perfil, name="perfil"),
    path('reserva/', mostrar_reserva, name="reserva"),
]