from django.db import models

# Create your models here.
class Mensaje(models.Model):
    remitente = models.CharField(max_length=200)
    destinatario = models.CharField(max_length=200)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'De {self.remitente}: {self.mensaje}'