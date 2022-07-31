from django.db import models
from .user import User
from .categoria import Categoria

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField('Descripción', max_length = 50)
    codigo = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, related_name='product', on_delete=models.CASCADE)
    precio_venta = models.IntegerField(default=0)
    existencias = models.IntegerField(default=0)