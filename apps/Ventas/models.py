
from django.db import models
import uuid

class Detalle_Venta(models.Model):
    id_detalle_venta = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    venta = models.ForeignKey('Ventas.Venta', on_delete=models.CASCADE)
    celular = models.ForeignKey('Celulares.Celular', on_delete=models.CASCADE)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.celular} - {self.precio_unitario}"
    
    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalles de Ventas'
        db_table = 'Detalle_Venta'

class Venta(models.Model):
    id_venta = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha = models.DateField(auto_now_add=True)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    usuario = models.ForeignKey('Usuarios.Usuario', on_delete=models.CASCADE)
    cliente = models.ForeignKey('Clientes.Cliente', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Venta {self.fecha} - Cliente: {self.cliente}"

    
    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table = 'Venta'
# Create your models here.
