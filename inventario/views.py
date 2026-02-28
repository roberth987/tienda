from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from inventario.models import Producto
from inventario.serializers import ProductoSerializer, CategoriaSerializer

# Create your views here.
class InventarioListView(APIView):
    def get(self, request):
        nombre = self.request.query_params.get("nombre")
        categoria = self.request.query.get("categoria")
        data = Producto.objects.all()
        import ipdb; ipdb.set_trace()
        if nombre:
            data.filter(nombre__icontains=nombre)

        if categoria:
            data.filter(categoria__nombre__incontains=categoria)

        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(data, request)
        serializer = ProductoSerializer(data, many=True)
        #ipdb.set_trace()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        print(request.data)
        serializer = ProductoPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class InventarioDetailView(APIView):
    def get(self, request, pk=None):
        try:
            data = Producto.objects.get(pk=pk)
            serializer = ProductoSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Producto.DoesNotExist:
            Response(data={"message": "el producto no existe"},
                     status=status.HTTP_404_NOT_FOUND)
    def put(self, request, pk=None):
        #Primero es consultar si el registro que se busca existe
        #Si no existe devuelvo un error
        #Serializar lo que viene en la peticion reques.data
        #editan dicho registro
        #Devuelven una respuesta si se edito con exito
        try:
            data= Producto.objects.get(pk=pk)
            serializer = ProductoPostSerializer(data, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"message":"producto editado"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Producto.DoesNotExist:
            return Response({"message":"No se encontro el producto"}, status=status.HTTP_404_NOT_FOUND)
        
    def patch(self, request, pk=None):
        try:
            data= Producto.objects.get(pk=pk)
            serializer = ProductoPostSerializer(data, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"message":"producto editado"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Producto.DoesNotExist:
            return Response({"message":"No se encontro el producto"}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk=None):
        #Primero es consultar si el registro que se busca existe
        #si no existe devuelvo un error
        #si existe se borra el producto
        try:
            data= Producto.objects.get(pk=pk)
            data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Producto.DoesNotExist:
            return Response({"message":"No se encontro el producto"}, status=status.HTTP_404_NOT_FOUND)
        
class CategoriaDetailView(APIView):
    def get(self, request, pk=None):
        try:
            data = Categoria.objects.get(pk=pk)
            serializer = CategoriaSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Categoria.DoesNotExist:
            return Response(data={"message": "la categoria no existe"},
                     status=status.HTTP_404_NOT_FOUND)
    def put(self, request, pk=None):
        try:
            data= Categoria.objects.get(pk=pk)
            serializer = CategoriaSerializer(data, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"message":"categoria editado"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Producto.DoesNotExist:
            return Response({"message":"No se encontro el categoria"}, status=status.HTTP_404_NOT_FOUND)
        
    def patch(self, request, pk=None):
        try:
            data= Categoria.objects.get(pk=pk)
            serializer = CategoriaSerializer(data, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"message":"categoria editado"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Categoria.DoesNotExist:
            return Response({"message":"No se encontro el categoria"}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk=None):
        pass