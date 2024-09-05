from django.shortcuts import get_object_or_404, render, redirect
from .models import Mensaje
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request,user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'auth.html', {'form':form, 'is_login':False})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'auth.html', {'form': form, 'is_login': True})

def user_logout(request):
    logout(request)  # Cierra la sesión del usuario actual
    return redirect('login')  # Redirige a la página principal después del cierre de sesión

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def CrearMensajes(request):
    if request.method == 'POST':
        remitente = request.user.username
        destinatario = request.POST.get('destinatario')
        mensaje = request.POST.get('mensaje')
        if destinatario and mensaje:
            nuevomensaje = Mensaje(remitente=remitente, destinatario=destinatario, mensaje=mensaje)
            nuevomensaje.save()
            return redirect('home')
    return render(request, 'crear.html')        

@login_required
def VerMensajes(request):
    mensajes = Mensaje.objects.filter(remitente=request.user.username) | Mensaje.objects.filter(destinatario=request.user.username)
    return render(request, 'mensajes.html', {'mensajes': mensajes})

def EliminarMensaje(request, mensaje_id):
    mensaje = get_object_or_404(Mensaje, id = mensaje_id)
    if mensaje.remitente == request.user.username or mensaje.destinatario == request.user.username:
        mensaje.delete
    return redirect('mensajes')