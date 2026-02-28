from rest_framework import serializers
from inventario.models import Producto, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '_all_'

class ProductoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)
    class Meta:
        model = Producto
        fields = '_all_'

class ProductoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ("nombre", "descripcion", "categoria", "cantidad")