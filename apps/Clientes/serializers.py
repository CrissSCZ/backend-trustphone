from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Cliente
        fields = ['id_cliente', 'nombre', 'apellido', 'email', 'carnet', 'activo', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        cliente = Cliente.objects.create(**validated_data)
        cliente.password = password  # Aquí deberías usar set_password en producción
        cliente.save()
        return cliente

class ClienteGoogleSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=100)
    apellido = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    carnet = serializers.CharField(max_length=20, required=False)

    def validate_email(self, value):
        if Cliente.objects.filter(email=value).exists():
            raise serializers.ValidationError('Este email ya está registrado')
        return value

    def validate_carnet(self, value):
        if value and Cliente.objects.filter(carnet=value).exists():
            raise serializers.ValidationError('Este carnet ya está registrado')
        return value

    def create(self, validated_data):
        try:
            cliente = Cliente.objects.create(
                nombre=validated_data['nombre'],
                apellido=validated_data['apellido'],
                email=validated_data['email'],
                carnet=validated_data.get('carnet', ''),
                activo=True
            )
            return cliente
        except Exception as e:
            raise serializers.ValidationError(str(e))
