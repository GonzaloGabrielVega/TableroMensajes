from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mensajes.urls')), #se incluyen todas las vistas incluidas en el urls.py de la app
]
