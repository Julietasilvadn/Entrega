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
    path('eliminarusuario/<usuario_nombre>/', views.eliminarUsuario, name="EliminarUsuario"),
    path('editarusuario/<usuario_nombre>/', views.editarUsuario, name='EditarUsuario'),
    path('list/', views.ListUsuario.as_view(), name='lista'),
    path('detalle/', views.DetalleUsuario.as_view(), name='Detalle'),
    path(r'^nuevo$', views.CreateUsuario.as_view(), name='Nuevo'),
    path(r'^editar/(?P<pk>\d+)$', views.UpdateUsuario.as_view(), name='Editar'),
    path(r'^borrar/(?P<pk>\d+)$', views.DeleteUsuario.as_view(), name='Eliminar'),
    path('mascotas/', mostrar_mascotas, name='mascotas'),
    path('perfil/', mostrar_perfil, name='perfil'),
    path('reserva/', mostrar_reserva, name='reserva'),
    path('registro/', mostrar_registro, name='registro'),
    path('formulario/registro/', registrarse_formulario, name= 'formulario'),
    ]