from django.urls import path
from apps.Tiendas.views import TiendaListView, CelularesPorTiendaView

urlpatterns = [
    path('tiendas/', TiendaListView.as_view(), name='tienda-list'),
    path('tiendas/<uuid:id_tienda>/celulares/', CelularesPorTiendaView.as_view(), name='celulares-por-tienda'),
]
