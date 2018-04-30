from django.db import models

# Create your models here.

    class Museo(models.Model):
        nombre = models.CharField(max_length=32)
        direccion = models.CharField(max_length=64)
        descripcion = models.TextField()
        barrio = models.CharField(max_length=32)
        distrito = models.CharField(max_length=32)
        accesibilidad = models.IntegerField()
        telefono = models.BigIntegerField()
        fax = models.BigIntegerField()
        email = models.CharField(max_liength=64)
        def __str__(self):
            return self.nombre

    class Seleccion(models.Model)
        usuario = models.ForeignKey(Usuario)
        museo = models.ForeignKey(Museo)
        def __str__(self):
            return self.museo

    class Comentario(models.Model)
        comentario = models.Textfield()
        museo = models.ForeignKey(Museo)
        usuario = ForeignKey(Usuario)
        fecha = models.DateTimeField(default = timezone.now())
        def __str__(self):
            return self.usuario.nombre

    class Usuario(models.Model)
        nombre = models.OneToOneField(User)
        contraseña = models.CharField(max_length=16)
        color = models.CharField(max_length=16)
        tamaño = models.IntegerField()
        fondo = models.CharField(max_length=16)
        titulo = models.CharField(max_length=16)
        def __str__(self):
            return self.nombre
        
