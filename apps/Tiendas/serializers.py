from rest_framework import serializers
from apps.Tiendas.models import Tienda
from apps.Celulares.models import Celular
from apps.Encargados.models import Encargado

class EncargadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encargado
        fields = '__all__'

class TiendaSerializer(serializers.ModelSerializer):
    encargado = serializers.SerializerMethodField()

    class Meta:
        model = Tienda
        fields = '__all__'

    def get_encargado(self, obj):
        try:
            encargado = obj.encargado
            return EncargadoSerializer(encargado).data
        except Encargado.DoesNotExist:
            return None

class CelularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Celular
        fields = '__all__'