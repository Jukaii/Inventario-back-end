from django.db import models
from .user import User
from .categoria import Categoria

class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField('Descripción', max_length = 50)
    categoria = models.ForeignKey(Categoria, related_name='product', on_delete=models.CASCADE)
    precio_venta = models.IntegerField(default=0)
    cantidad = models.IntegerField(default=0)