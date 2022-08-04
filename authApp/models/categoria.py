from django.db import models

class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    nombreCategoria= models.CharField(max_length = 50)