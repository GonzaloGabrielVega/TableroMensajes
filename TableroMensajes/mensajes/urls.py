from django.urls import path
from . import views

urlpatterns = [
    path('', views.CrearMensajes, name='crear'),
]