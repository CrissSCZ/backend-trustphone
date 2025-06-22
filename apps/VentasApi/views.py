
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status   
from apps.VentasApi.serializers import VentaSerializer
from apps.Ventas.models import Venta, Detalle_Venta
from apps.Clientes.models import Cliente
from apps.Tiendas.models import Tienda
from apps.Tiendas.serializers import TiendaSerializer
from apps.Usuarios.models import Usuario
from .serializers import UsuarioSerializer

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
    
class ObtenerRecibo(APIView):
    def get(self, request, id_cliente, id_venta):
        try:
            cliente = Cliente.objects.get(id_cliente=id_cliente)
            ventas = Venta.objects.filter(cliente=cliente, id_venta=id_venta).order_by('-fecha')
            serializer_venta = VentaSerializer(ventas, many=True)

            venta = ventas.first()
            if not venta:
                return Response({"error": "Venta no encontrada"}, status=status.HTTP_404_NOT_FOUND)

            usuario = Usuario.objects.get(id_usuario=venta.usuario.id_usuario)
            detalle = Detalle_Venta.objects.filter(venta=venta).first()
            tienda = Tienda.objects.get(id_tienda=detalle.celular.tienda.id_tienda)

            serializer_usuario = UsuarioSerializer(usuario)
            serializer_tienda = TiendaSerializer(tienda)

            response_data = {
                'venta': serializer_venta.data[0],
                'usuario': serializer_usuario.data,
                'tienda': serializer_tienda.data
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except Cliente.DoesNotExist:
            return Response({"error": "Cliente no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        except Venta.DoesNotExist:
            return Response({"error": "Venta no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        except Tienda.DoesNotExist:
            return Response({"error": "Tienda no encontrada"}, status=status.HTTP_404_NOT_FOUND)
