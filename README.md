# Proyecto Django para renderizacion de usuarios

## Creacion de Proyecto

_Comandos necesarios para la creacion de proyecto en Django_

```
django-admin startproject nombre_proyecto .
python manage.py startapp core
python manage.py migrate 
Agregar app nueva al archivo settings.py
```

_Comandos necesarios para crear usuario administrador de BBDD en Django_
```
python manage.py createsuperuser --email admin@correo.cl --username nombre_usuario
```