from django.db import models
from .user import User

class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    userRol = models.ForeignKey(User, related_name='FKid', on_delete=models.CASCADE)
    status = models.CharField('status', max_length = 30)
    rol = models.CharField('rol', max_length = 30)