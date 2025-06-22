from django.urls import path
from .views import ObtenerVentas, ObtenerVentasCliente, ObtenerRecibo

urlpatterns = [
    path('', ObtenerVentas.as_view(), name='obtener_ventas'),
    path('<uuid:id_cliente>/compras', ObtenerVentasCliente.as_view(), name='obtener_ventas_cliente'),
    path('<uuid:id_cliente>/compras/<uuid:id_venta>', ObtenerRecibo.as_view(), name='obtener_recibo'),
]