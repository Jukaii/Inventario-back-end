from rest_framework import serializers
from authApp.models import categoria

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoria.Categoria
        fields = ['idCategoria', 'nombreCategoria']
