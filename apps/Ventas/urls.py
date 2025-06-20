from django.urls import path, include
from .views import main, crear_venta, obtener_venta

urlpatterns = [
    path('', main, name='ventas'),
    path('crear_venta/', crear_venta, name='crear_venta'),
    path('obtener_venta/<uuid:id_venta>', obtener_venta, name='obtener_venta')
]
