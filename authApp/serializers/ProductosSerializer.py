from rest_framework import serializers
from authApp.models import productos

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model= productos.Productos
        fields = ['idProducto', 'nombre', 'precio_venta', 'existencias', 'categoria', 'idUsuario']