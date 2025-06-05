from django.db import models
import uuid
class Tienda(models.Model):
    id_tienda = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    detalles = models.TextField(max_length=500)
    fotografia = models.ImageField(upload_to='tiendas')
    encargado = models.ForeignKey('Encargados.Encargado', on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Tienda'
        verbose_name_plural = 'Tiendas'
        db_table = 'Tienda'
    
# Create your models here.
