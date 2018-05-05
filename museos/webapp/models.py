from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone


# Create your models here.

class Museo(models.Model):
    nombre = models.CharField(max_length=32)
    direccion = models.CharField(max_length=64)
    enlace = models.CharField(max_length=512)
    descripcion = models.TextField()
    barrio = models.CharField(max_length=32)
    distrito = models.CharField(max_length=32)
    accesibilidad = models.CharField(max_length=32)
    telefono = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.OneToOneField(User,related_name="usuario")
    color = models.CharField(max_length=16)
    tamaño = models.IntegerField()
    fondo = models.CharField(max_length=16)
    titulo = models.CharField(max_length=16)
    def __str__(self):
        return self.nombre.username

class Seleccion(models.Model):
    usuario = models.ForeignKey(Usuario)
    museo = models.ForeignKey(Museo)
    fecha = models.DateTimeField(default = timezone.now())
    def __str__(self):
        return self.museo

class Comentario(models.Model):
    comentario = models.TextField()
    museo = models.ForeignKey(Museo)
    usuario = models.ForeignKey(Usuario)
    fecha = models.DateTimeField(default = timezone.now())
    def __str__(self):
        return self.usuario.nombre.username
        
