
from authApp.models import productos
from authApp.serializers import ProductosSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def prod_lista(request):
    # obtenemos todos los productos
    # serializamos
    # devolvemos Json
    if request.method == 'GET':
        prodts=productos.Productos.objects.all()
        serializer = ProductosSerializer(prodts, many=True)
        return Response(serializer.data)

    if request.method == 'POST':  
        serializer = ProductosSerializer(data=request.data)   
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)    

@api_view(['GET','PUT','DELETE'])
def detalles_producto(request, id):

    try:
        producto = productos.Productos.objects.get(pk=id) 
    except productos.Productos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    
    if request.method == 'GET':
        serializer = ProductosSerializer(producto) 
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProductosSerializer(producto,data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
    elif request.method == 'DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
