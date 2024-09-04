from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.CrearMensajes, name='crear'),
    path('mensajes/', views.VerMensajes, name='mensajes')
]