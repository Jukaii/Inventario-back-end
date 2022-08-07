from rest_framework.views import APIView
from rest_framework.response import Response
from authApp.serializers.CategoriasSerializer import CategoriasSerializer
from authApp.models.categoria import Categoria

class CategoriasView(APIView):
    serializer_class = CategoriasSerializer
    def get(self, request):
        categoria = Categoria.objects.all()
        categoria_serializer = CategoriasSerializer(categoria, many = True)
        return Response(categoria_serializer.data)
    
    def post(self, request):
        categoria_serializer = CategoriasSerializer(data = request.data)
        if categoria_serializer.is_valid():
            categoria_serializer.save()
            return Response("Categoria Guardada Correctamente")
        return Response(categoria_serializer.errors)

class CategoriaDetail(APIView):
    def get(self,request, pk=None):
        categoria = Categoria.objects.filter(idCategoria = pk).first()
        categoria_serializer = CategoriasSerializer(categoria)
        return Response(categoria_serializer.data)

    def put(self,request, pk= None):
        categoria = Categoria.objects.filter(idCategoria = pk).first()
        categoria_serializer = CategoriasSerializer(categoria, data = request.data)
        if categoria_serializer.is_valid():
            categoria_serializer.save()
            return Response("Nombre de Categoria Actualizado")
        return Response(categoria_serializer.errors)
    
    def delete(self,request,pk):
        categoria = Categoria.objects.filter(idCategoria = pk).first()
        msg = f'Se ha eliminado la categoria con Id: {categoria.idCategoria}'
        categoria.delete()
        return Response(msg)