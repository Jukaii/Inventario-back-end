from rest_framework import serializers


from authApp.models import productos

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model=productos.Productos
        campos=['id','nombre','descripcion','categoria','precio de venta','numero de existencias']