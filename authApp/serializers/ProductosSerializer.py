from rest_framework import serializers
from models import productos

from authApp.models import productos

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model=productos
        campos=['nombre','id','descripcion','categoria','precio de venta','numero de existencias']