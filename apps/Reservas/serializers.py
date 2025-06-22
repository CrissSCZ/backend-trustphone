from apps.Clientes.models import Cliente
from apps.Celulares.models import Celular
from apps.Reservas.models import Reserva
from rest_framework import serializers

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente  # Asegúrate de importar Cliente
        fields = '__all__'

class CelularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Celular
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)
    celular = CelularSerializer(read_only=True)

    class Meta:
        model = Reserva
        fields = ['id_reserva', 'comprobante', 'fecha', 'estado', 'cliente', 'celular']
