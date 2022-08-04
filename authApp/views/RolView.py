from rest_framework.views import APIView
from rest_framework.response import Response
from authApp.serializers.RolSerializer import RolSerializer
from authApp.models.rol import Rol

class RolView(APIView):
    serializer_class = RolSerializer
    def get(self, request):
        rol = Rol.objects.all()
        rol_serializer = RolSerializer(rol, many = True)
        return Response(rol_serializer.data)
    
    def post(self, request):
        rol_serializer = RolSerializer(data = request.data)
        if rol_serializer.is_valid():
            rol_serializer.save()
            return Response("Rol Guardado Correctamente")
        return Response(rol_serializer.errors)

class RolDetail(APIView):
    def get(self,request, pk=None):
        rol = Rol.objects.filter(id = pk).first()
        rol_serializer = RolSerializer(rol)
        return Response(rol_serializer.data)

    def put(self,request, pk= None):
        rol = Rol.objects.filter(id = pk).first()
        rol_serializer = RolSerializer(rol, data = request.data)
        if rol_serializer.is_valid():
            rol_serializer.save()
            return Response("Rol Actualizado")
        return Response(rol_serializer.errors)
    
    def delete(self,request,pk):
        rol = Rol.objects.filter(id = pk).first()
        msg = f'Se ha eliminado el rol con Id: {rol.id}'
        rol.delete()
        return Response(msg)