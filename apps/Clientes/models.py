from django.db import models
import uuid
class Cliente(models.Model):
    id_cliente = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    carnet = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)  # Almacenamos la contraseña encriptada
    activo = models.BooleanField(default=True)
    
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'Cliente'
