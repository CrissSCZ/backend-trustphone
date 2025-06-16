from rest_framework import serializers
from apps.Celulares.models import Celular, ImagenCelular
from apps.Tiendas.models import Tienda
from apps.Marcas.models import Marca
from apps.Vendedores.models import Vendedor

class ImagenCelularSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenCelular
        fields = ['id_imagen', 'imagen', 'orden']

class CelularSerializer(serializers.ModelSerializer):
    imagenes = ImagenCelularSerializer(many=True, read_only=True)
    
    class Meta:
        model = Celular
        fields = '__all__'
