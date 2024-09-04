from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('crear/', views.CrearMensajes, name='crear'),
    path('mensajes/', views.VerMensajes, name='mensajes'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]