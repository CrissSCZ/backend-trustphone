from django.db import models
import uuid

class Marca(models.Model):
    id_marca = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        db_table = 'Marca'

class Celular(models.Model):
    ram_choices = (
        (4, '4GB'),
        (6, '6GB'),
        (8, '8GB'),
        (12, '12GB'),
        (16, '16GB'),
    )
    estado_venta_choices = (
        (0, 'Disponible'),
        (1, 'Vendido'),
        (2, 'Reservado'),
    )
    almacenamiento_choices = (
        (8, '8GB'),
        (16, '16GB'),
        (32, '32GB'),
        (64, '64GB'),
        (128, '128GB'),
        (256, '256GB'),
        (512, '512GB'),
        (1024, '1TB'),
    )
    
    estado_choices = (
        (0, 'Como nuevo'),
        (1, 'Detalles esteticos'),
        (2, 'Detalles Fuertes')
    )
    
    id_celular = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    imagenes = models.ImageField(upload_to='celulares', null=False, blank=False)
    modelo = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    almacenamiento = models.IntegerField(choices=almacenamiento_choices)
    ram = models.IntegerField(choices=ram_choices)
    estado = models.IntegerField(choices=estado_choices)
    detalles = models.TextField(max_length=500)
    imei = models.CharField(max_length=15, unique=True)
    imei2 = models.CharField(max_length=15, unique=True, null=True)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    precio_minimo = models.DecimalField(max_digits=10, decimal_places=2)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE)
    tienda = models.ForeignKey('Tiendas.Tienda', on_delete=models.CASCADE)
    vendedor = models.ForeignKey('Vendedores.Vendedor', on_delete=models.CASCADE)
    estado_venta = models.IntegerField(choices=estado_venta_choices, default=0)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.modelo
    
    class Meta:
        verbose_name = 'Celular'
        verbose_name_plural = 'Celulares'
        db_table = 'Celular'
    
# Create your models here.
