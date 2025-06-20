from django.urls import path
from .views import main, crear_venta, generar_recibo

urlpatterns = [
    path('', main, name='ventas'),
    path('crear_venta/', crear_venta, name='crear_venta'),
    path('generar_recibo/<uuid:id_venta>', generar_recibo, name='generar_recibo'),
]
