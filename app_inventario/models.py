from django.db import models


#se encarga de crear las tablas, en esta caso la de inventario
class inventario(models.Model):
    referencia = models.CharField(max_length = 50)
    marca =  models.IntegerField(models.ForeignKey("app.Model", verbose_name=(""), on_delete=models.CASCADE))
    diametro = models.IntegerField()
    categoria = models.IntegerField(models.ForeignKey("app.Model", verbose_name=(""), on_delete=models.CASCADE))
    descripcion =models.CharField(max_length = 500)
    estado = models.IntegerField(models.ForeignKey("app.Model", verbose_name=(""), on_delete=models.CASCADE))
    def __str__(self):
        return self.referencia

#se encarga de crear las tablas, en esta caso la de marca
class marca(models.Model):
    nombre_marca = models.CharField(max_length = 50)
    referencia = models.CharField(max_length = 50)
    def __str__(self):
        return self.nombre_marca

#se encarga de crear las tablas, en esta caso la de categoria
class categoria(models.Model):
    categoria = models.CharField(max_length = 50)
    marca = models.CharField(max_length = 50)
    referencia = models.CharField(max_length = 50)
    def __str__(self):
        return self.categoria

#se encarga de crear las tablas, en esta caso la de estado
class estado(models.Model):
    estado = models.CharField(max_length = 50)
    categoria = models.CharField(max_length = 50)
    marca = models.CharField(max_length = 50)
    referencia = models.CharField(max_length = 50)
    def __str__(self):
        return self.estado