from django.db import models
import uuid
class Encargado(models.Model):
    id_encargado = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    carnet = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre + " " + self.apellido
    
    class Meta:
        verbose_name = 'Encargado'
        verbose_name_plural = 'Encargados'
        db_table = 'Encargado'
# Create your models here.
