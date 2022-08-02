from django.http import JsonResponse
from authApp.models import productos
from models import Productos
from serializers import ProductosSerializer

def prod_lista(request):
    # obtenemos todos los productos
    # serializamos
    # devolvemos Json
    productos=Productos.objects.all()
    serializer = ProductosSerializer(productos, many=True)
    return JsonResponse(serializer.data)