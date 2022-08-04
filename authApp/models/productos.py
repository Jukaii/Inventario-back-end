from django.db import models
from .user import User
from .categoria import Categoria

class Productos(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombre = models.CharField('NombreProducto', max_length = 50)
    precio_venta = models.FloatField(null=True)
    existencias = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, related_name='FKidCategoria', on_delete=models.CASCADE)
    idUsuario = models.ForeignKey(User, related_name='FKidUser', on_delete=models.CASCADE)