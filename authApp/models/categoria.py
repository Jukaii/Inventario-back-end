from django.db import models
from .user import Products

class Categoria():
    id = models.AutoField(primary_key=True)
    nombre=models.CharField(max_length = 50)
