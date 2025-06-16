from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import GoogleAuthSerializer
from .models import Usuario

class GoogleAuthView(APIView):
    def post(self, request):
        serializer = GoogleAuthSerializer(data=request.data)
        if serializer.is_valid():
            try:
                # Intentar obtener el usuario existente
                usuario = Usuario.objects.get(id_usuario=serializer.validated_data['id'])
                return Response({
                    'message': 'Usuario ya existe',
                    'user': {
                        'id': usuario.id_usuario,
                        'email': usuario.usuario,
                        'role': usuario.rol
                    }
                }, status=status.HTTP_200_OK)
            except Usuario.DoesNotExist:
                # Crear nuevo usuario
                usuario = serializer.save()
                return Response({
                    'message': 'Usuario creado exitosamente',
                    'user': {
                        'id': usuario.id_usuario,
                        'email': usuario.usuario,
                        'role': usuario.rol
                    }
                }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
