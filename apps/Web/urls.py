from django.urls import path, include
from .views import admin, login_view, logout_view

urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', admin, name='administrador'),

    path('celulares/', include(('apps.Celulares.urls'))),
    path('vendedores/', include(('apps.Vendedores.urls'))),
    path('configuracion/', include(('apps.Configuracion.urls'))),
    path('clientes/', include(('apps.Clientes.urls'))),
    path('dashboard/', include(('apps.Dashboard.urls'))),
    path('ventas/', include(('apps.Ventas.urls'))),
    path('reservas/', include(('apps.Reservas.urls'))),
]
