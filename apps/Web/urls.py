from django.urls import path, include
from .views import admin, login_view, logout_view

urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('panel/', admin, name='administrador'),

    path('celulares/', include(('apps.Celulares.urls'))),
    path('vendedores/', include(('apps.Vendedores.urls'))),
    path('configuracion/', include(('apps.Configuracion.urls'))),
]
