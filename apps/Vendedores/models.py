from django.db import models
import uuid
class Vendedor(models.Model):
    id_vendedor = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre + " " + self.apellido
    
    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'
        db_table = 'Vendedor'
# Create your models here.
