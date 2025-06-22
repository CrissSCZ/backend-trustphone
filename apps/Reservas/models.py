from django.db import models
import uuid

class Reserva(models.Model):
    ESTADO_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('terminada', 'Terminada'),
    )
    id_reserva = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cliente = models.ForeignKey('Clientes.Cliente', on_delete=models.CASCADE)
    celular = models.ForeignKey('Celulares.Celular', on_delete=models.CASCADE)
    comprobante = models.ImageField(upload_to='comprobantes/', blank=True, null=True)
    fecha = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=20, default='pendiente', choices=ESTADO_CHOICES)
    def __str__(self):
        return f"Reserva {self.fecha} - {self.cliente} - {self.celular}"

# Create your models here.
