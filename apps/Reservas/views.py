from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.Clientes.models import Cliente
from apps.Celulares.models import Celular
from apps.Reservas.models import Reserva
from apps.Reservas.serializers import ReservaSerializer
from apps.Ventas.models import Venta
from apps.Ventas.models import Detalle_Venta
from apps.Usuarios.models import Usuario
from apps.Ventas.views import generar_recibo

class ListaReservas(APIView):
    def get(self, request):
        reservas = Reserva.objects.all()
        serializer = ReservaSerializer(reservas, many=True)
        return Response(serializer.data)
    
class ReservasCliente(APIView):
    def get(self, request, id_cliente):
        cliente = Cliente.objects.get(id_cliente=id_cliente)
        reservas = Reserva.objects.filter(cliente=cliente)
        serializer = ReservaSerializer(reservas, many=True)
        return Response(serializer.data)

class CrearReserva(APIView):
    def post(self, request, id_cliente):
        try:
            cliente = Cliente.objects.get(id_cliente=id_cliente)
            required_fields = ['celular', 'comprobante']
            missing_fields = [field for field in required_fields if field not in request.data]
            
            if missing_fields:
                return Response(
                    {'error': f'Faltan campos requeridos: {", ".join(missing_fields)}'},
                    status=status.HTTP_400_BAD_REQUEST
                )
                
            id_celular = request.data.get('celular')
            try:
                celular = Celular.objects.get(id_celular=id_celular)
            except Celular.DoesNotExist:
                return Response(
                    {'error': 'Celular no encontrado'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            reserva = Reserva(
                cliente=cliente,
                celular=celular,
                comprobante=request.data.get('comprobante'),
                estado='pendiente'
            )
            celular.estado_venta = 2
            celular.save()
            
            reserva.save()
            
            serializer = ReservaSerializer(reserva)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        except Cliente.DoesNotExist:
            return Response(
                {'error': 'Cliente no encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
def main(request):
    reservas = Reserva.objects.all()
    return render(request, 'modules/reservas/index.html', {'reservas': reservas})

def terminar_reserva(request, id_reserva):
    reserva = Reserva.objects.get(id_reserva=id_reserva)
    celular = reserva.celular
    email_usuario = request.session['user_email']
    usuario = Usuario.objects.get(email=email_usuario)

    venta = Venta.objects.create(
        cliente=reserva.cliente,
        usuario=usuario,
        descuento=0,
        total=0
    )

    Detalle_Venta.objects.create(
        venta=venta,
        celular=celular,
        precio_unitario=celular.precio
    )

    celular.estado_venta = 1
    celular.save()

    venta.total = celular.precio
    venta.save()
    reserva.estado = 'terminada'
    reserva.save()

    generar_recibo(request, venta.id_venta)

    return redirect('ventas')

def ver_reserva(request, id_reserva):
    reserva = Reserva.objects.get(id_reserva=id_reserva)
    return render(request, 'modules/reservas/ver_reserva.html', {'reserva': reserva})
