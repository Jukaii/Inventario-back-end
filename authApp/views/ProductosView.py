from rest_framework.views import APIView
from rest_framework.response import Response
from authApp.serializers.ProductosSerializer import ProductosSerializer
from authApp.models.productos import Productos


class ProductosView(APIView):
    serializer_class = ProductosSerializer
    def get(self, request):
        productos = Productos.objects.all()
        productos_serializer = ProductosSerializer(productos, many = True)
        return Response(productos_serializer.data)
    
    def post(self, request):
        productos_serializar = ProductosSerializer(data = request.data)
        if productos_serializar.is_valid():
            productos_serializar.save()
            return Response("Producto Guardado Correctamente")
        return Response(productos_serializar.errors)
    
class ProductosDetail(APIView):
    def get(self,request, pk=None):
        productos = Productos.objects.filter(idProducto = pk).first()
        Productos_serializer = ProductosSerializer(productos)
        return Response(Productos_serializer.data)

    def put(self,request, pk= None):
        productos = Productos.objects.filter(idProducto = pk).first()
        Productos_serializer = ProductosSerializer(productos, data = request.data)
        if Productos_serializer.is_valid():
            Productos_serializer.save()
            return Response("Producto Actualizado")
        return Response(Productos_serializer.errors)
    
    def delete(self,request,pk):
        productos = Productos.objects.filter(idProducto = pk).first()
        msg = f'Se ha eliminado el producto con Id: {productos.idProducto}'
        productos.delete()
        return Response(msg)