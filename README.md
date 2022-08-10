# Entrega

# VIDEO: https://youtu.be/GvsB8qndMEw

# Integrantes:
- Juan Echenique: creación de modelos, elección de bootstrap, login
- Julieta Silva: herencia html, inicio de proyecto y aplicación, aplicación con estilo de bootstrap, corrección de formularios y modelos, casos de prueba, about, readme, video
- Lara Dipre: corrección de formularios y modelos, crud, avatar, casos de prueba, readme, about, video, login, creación de templates

**Sistema de gestión de contenidos**
Este proyecto tiene como objetivo crear un sistema para administrar una peluquería para mascotas. Es posible realizar:
- Crear, leer, actualizar y eliminar el Usuario
- Agregar un avatar

*Instalar*
Este proyecto fue escrito con python versión 3.9.12, se recomienda utilizar la misma versión para no tener problemas de compatibilidad.

Para chequear la version de python, en su sistema escribir:

- Si cuenta con sistema *nix:
> python --version
> Python 3.9.12

- Si tiene windows:
c:\> py --version
c:\> Python 3.9.12

*Configurando la aplicación de django*
Es necesario correr algunos comandos para hacer funcionar la app.
1. Migraciones
        - Iniciar la base de datos en Windows:

c:\> python manage.py migrate

2. Correr el test server

        - windows:

c:\> python manage.py runserver

Si todo funciona perfecto, será capaz de abrir el navegador y ver la aplicación correr. 


