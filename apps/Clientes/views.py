from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ClienteGoogleSerializer
from .models import Cliente

class ClienteGoogleAuthView(APIView):
    def post(self, request):
        try:
            serializer = ClienteGoogleSerializer(data=request.data)
            if serializer.is_valid():
                # Intentar obtener el cliente existente por email
                try:
                    cliente = Cliente.objects.get(email=serializer.validated_data['email'])
                    return Response({
                        'message': 'Cliente ya existe',
                        'cliente': {
                            'id': cliente.id_cliente,
                            'nombre': cliente.nombre,
                            'apellido': cliente.apellido,
                            'email': cliente.email,
                            'carnet': cliente.carnet,
                            'activo': cliente.activo
                        }
                    }, status=status.HTTP_200_OK)
                except Cliente.DoesNotExist:
                    # Crear nuevo cliente
                    cliente = serializer.save()
                    return Response({
                        'message': 'Cliente creado exitosamente',
                        'cliente': {
                            'id': cliente.id_cliente,
                            'nombre': cliente.nombre,
                            'apellido': cliente.apellido,
                            'email': cliente.email,
                            'carnet': cliente.carnet,
                            'activo': cliente.activo
                        }
                    }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'message': 'Datos inválidos',
                    'errors': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'message': 'Error interno del servidor',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
