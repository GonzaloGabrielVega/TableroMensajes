from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.user_login, name='login'),
    path('crear/', views.CrearMensajes, name='crear'),
    path('mensajes/', views.VerMensajes, name='mensajes'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('eliminar/<int:mensaje_id>/', views.EliminarMensaje, name='eliminar'),
]