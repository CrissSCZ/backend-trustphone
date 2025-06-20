from django.urls import path
from .views import ObtenerVentas, ObtenerVentasCliente

urlpatterns = [
    path('', ObtenerVentas.as_view(), name='obtener_ventas'),
    path('<uuid:id_cliente>/compras', ObtenerVentasCliente.as_view(), name='obtener_ventas_cliente'),
]