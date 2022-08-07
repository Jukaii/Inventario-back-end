from rest_framework import serializers
from authApp.models.user import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nombre', 'apellido', 'username', 'password', 'telefono', 'email']
        
    def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        return userInstance
        
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        return {
                'id': user.id,
                'nombre': user.nombre,
                'apellido': user.apellido,
                'username': user.username,
                'telefono': user.telefono,
                'email': user.email,
                }    