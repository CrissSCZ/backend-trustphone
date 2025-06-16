from rest_framework import serializers
from .models import Usuario

class GoogleAuthSerializer(serializers.Serializer):
    id = serializers.CharField()
    nombre = serializers.CharField()
    apellido = serializers.CharField()
    email = serializers.EmailField()
    picture = serializers.URLField()
    role = serializers.CharField()

    def validate_role(self, value):
        valid_roles = ['cliente', 'vendedor']
        if value not in valid_roles:
            raise serializers.ValidationError(f"Role must be one of: {', '.join(valid_roles)}")
        return value

    def create(self, validated_data):
        # Convertir el role de cliente/vendedor a admin/encargado/vendedor
        role_mapping = {
            'cliente': 'cliente',  # Mantener cliente como rol
            'vendedor': 'vendedor'
        }
        
        usuario = Usuario.objects.create(
            id_usuario=validated_data['id'],
            usuario=validated_data['email'],  # Usamos el email como usuario
            contrasena='',  # No necesitamos contraseña con Google Auth
            rol=role_mapping.get(validated_data['role'], 'cliente'),
            tienda=None,  # Se asignará cuando el usuario seleccione una tienda
            activo=True
        )
        return usuario
