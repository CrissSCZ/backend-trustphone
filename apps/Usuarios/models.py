from django.db import models
import uuid
class Usuario(models.Model):
    id_usuario = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True, blank=True)
    password = models.CharField(max_length=128, null=True, blank=True)
    rol = models.CharField(max_length=20, choices=[('admin', 'Administrador'), ('vendedor', 'Vendedor')])
    activo = models.BooleanField(default=True)
    tienda = models.ForeignKey('Tiendas.Tienda', on_delete=models.SET_NULL, null=True, blank=True, related_name='usuarios')
    
    def __str__(self):
        return f"{self.nombre} ({self.email})"
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'Usuario'
    
# Create your models here.
