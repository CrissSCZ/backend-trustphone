from rest_framework import serializers
from apps.Celulares.models import Celular
from apps.Ventas.models import Venta, Detalle_Venta
from apps.Clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class CelularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Celular
        fields = '__all__'

class DetalleVentaSerializer(serializers.ModelSerializer):
    celular = CelularSerializer()

    class Meta:
        model = Detalle_Venta
        fields = '__all__'

class VentaClienteSerializer(serializers.ModelSerializer):
    detalle_venta = serializers.SerializerMethodField()
    cliente = ClienteSerializer()

    class Meta:
        model = Venta
        fields = '__all__'

    def get_detalle_venta(self, obj):
        detalles = Detalle_Venta.objects.filter(venta=obj)
        return DetalleVentaSerializer(detalles, many=True).data

class VentaSerializer(serializers.ModelSerializer):
    detalle_venta = serializers.SerializerMethodField()
    cliente = ClienteSerializer()

    class Meta:
        model = Venta
        fields = '__all__'

    def get_detalle_venta(self, obj):
        detalles = Detalle_Venta.objects.filter(venta=obj)
        return DetalleVentaSerializer(detalles, many=True).data