from django.shortcuts import render, redirect
from .models import Mensaje

# Create your views here.
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