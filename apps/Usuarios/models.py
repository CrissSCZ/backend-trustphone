from django.db import models
import uuid
class Usuario(models.Model):
    id_usuario = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)
    rol_choices = (
        ('admin', 'Admin'),
        ('encargado', 'Encargado'),
        ('vendedor', 'Vendedor'),
    )
    rol = models.CharField(max_length=100, choices=rol_choices)
    tienda = models.ForeignKey('Tiendas.Tienda', on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.usuario
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'Usuario'
    
# Create your models here.
