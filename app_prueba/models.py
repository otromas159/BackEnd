from django.db import models

#se encarga de crear las tablas, en esta caso la de usuario
class usuarios(models.Model):
    nombre = models.CharField(max_length = 50)
    correo = models.EmailField()
    clave = models.CharField()
    tipo = models.IntegerField(models.ForeignKey("app.Model", verbose_name=(""), on_delete=models.CASCADE))
    def __str__(self):
        return self.nombre

#se encarga de crear las tablas, en esta caso la de tipo

class tipo(models.Model):
    nombre = models.CharField(max_length = 50)
    descripcion = models.CharField()
    def __str__(self):
        return self.nombre