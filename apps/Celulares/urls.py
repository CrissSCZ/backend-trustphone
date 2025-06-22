from django.urls import path
from .views import main, crear_celular, editar_celular, eliminar_celular

urlpatterns = [
    path('', main, name='celulares'),
    path('crear_celular/', crear_celular, name='crear_celular'),
    path('editar_celular/<uuid:id_celular>/', editar_celular, name='editar_celular'),
    path('eliminar_celular/<uuid:id_celular>/', eliminar_celular, name='eliminar_celular')
]
