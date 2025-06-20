
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status   
from apps.VentasApi.serializers import VentaSerializer
from apps.Ventas.models import Venta
from apps.Clientes.models import Cliente

class ObtenerVentasCliente(APIView):
    def get(self, request, id_cliente):
        try:
            cliente = Cliente.objects.get(id_cliente=id_cliente)
            ventas = Venta.objects.filter(cliente=cliente).order_by('-fecha')
            serializer = VentaSerializer(ventas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Cliente.DoesNotExist:
            return Response({"error": "Cliente no encontrado"}, status=status.HTTP_404_NOT_FOUND)

class ObtenerVentas(APIView):
    def get(self, request):
        ventas = Venta.objects.all().order_by('-fecha')
        serializer = VentaSerializer(ventas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)