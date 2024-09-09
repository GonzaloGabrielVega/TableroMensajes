# Tablero de Mensajes

Este proyecto consiste en una aplicación web desarrollada con Django para la gestión de mensajes, 
permitiendo a los usuarios crear, ver y eliminar mensajes de manera eficiente bajo un contexto de usuarios autenticados.

## Requisitos previos

Antes de comenzar con la instalación, asegúrate de tener las siguientes herramientas instaladas en tu entorno:

- Python 3.10.12
- Django 4.2
- pip (Administrador de paquetes de Python)
- Git (Opcional, para la gestión del código fuente)

## Instalación

Pasos para instalar el proyecto:

1. Clonar el repositorio:
      git clone https://github.com/GonzaloGabrielVega/TableroMensajes.git

2. Crear y activar un entorno virtual
    # Crear el entorno virtual
    python -m venv  

    # Activar el entorno virtual (en Linux)
    source venv/bin/activate

3. Instala las dependencias
    Dentro del entorno virtual, instala las dependencias necesarias ejecutando:
    
        pip install -r requirements.txt

## Uso

Para el uso y ejecución del programa ejecutar:

    Realizar las migraciones:

        python manage.py migrate
    
    Iniciar el servidor de Django:

        python manage.py runserver

    Abre tu navegador y accede a la aplicación en http://127.0.0.1:8000/.

## Funcionalidades

    - Creaer mensajes
    - Ver mensajes enviados y recibidos
    - eliminar mensajes

## Contacto 

    correo: ggvega@udc.edu.ar