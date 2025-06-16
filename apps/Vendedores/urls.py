from django.urls import path
from .views import crear_vendedor, editar_vendedor, eliminar_vendedor, main

urlpatterns = [
    path('', main, name='vendedores'),
    path('crear_vendedor', crear_vendedor, name='crear_vendedor'),
    path('editar_vendedor/<uuid:id_vendedor>', editar_vendedor, name='editar_vendedor'),
    path('eliminar_vendedor/<uuid:id_vendedor>', eliminar_vendedor, name='eliminar_vendedor'),
]   
