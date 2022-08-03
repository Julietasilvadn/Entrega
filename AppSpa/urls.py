from msilib.schema import AdminExecuteSequence
from ssl import VERIFY_ALLOW_PROXY_CERTS
from django.contrib import admin
from django.urls import path
from AppSpa.views import base
from . import views 

urlpatterns = [
    path('inicio', base, name = 'Inicio'),
    path('suscripcion/', views.inscripcion, name='Inscripcion Cliente'),
]