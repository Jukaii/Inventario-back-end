from rest_framework import serializers


from authApp.models import productos

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model=productos.Productos
        fields =['id','descripcion','categoria','precio_venta','cantidad']