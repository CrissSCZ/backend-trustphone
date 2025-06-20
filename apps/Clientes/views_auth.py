from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cliente
from .serializers import ClienteSerializer

class ClienteLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            cliente = Cliente.objects.get(email=email)
            if cliente.password == password:
                return Response({
                    'message': 'Inicio de sesión exitoso',
                    'cliente': {
                        'id': str(cliente.id_cliente),
                        'nombre': cliente.nombre,
                        'apellido': cliente.apellido,
                        'email': cliente.email,
                        'carnet': cliente.carnet,
                        'activo': cliente.activo
                    }
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'message': 'Email o contraseña incorrectos'
                }, status=status.HTTP_401_UNAUTHORIZED) 
        except Cliente.DoesNotExist:
            return Response({
                'message': 'Email o contraseña incorrectos'
            }, status=status.HTTP_401_UNAUTHORIZED)

class ClienteRegisterView(APIView):
    def post(self, request):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            try:
                cliente = serializer.save()
                return Response({
                    'message': 'Registro exitoso',
                    'cliente': {
                        'id': str(cliente.id_cliente),
                        'nombre': cliente.nombre,
                        'apellido': cliente.apellido,
                        'email': cliente.email,
                        'carnet': cliente.carnet,
                        'activo': cliente.activo
                    }
                }, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({
                    'message': 'Error al registrar',
                    'error': str(e)
                }, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
