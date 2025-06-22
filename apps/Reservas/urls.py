from django.urls import path
from .views import ListaReservas, ReservasCliente, CrearReserva, main, terminar_reserva, ver_reserva
urlpatterns = [
    path('', ListaReservas.as_view(), name='lista-reservas'),
    path('<uuid:id_cliente>/', ReservasCliente.as_view(), name='reservas-cliente'),
    path('<uuid:id_cliente>/crear/', CrearReserva.as_view(), name='crear-reserva'),    
    path('listar/', main, name='reservas'),
    path('terminar_reserva/<uuid:id_reserva>/', terminar_reserva, name='terminar_reserva'),
    path('ver_reserva/<uuid:id_reserva>/', ver_reserva, name='ver_reserva')
]