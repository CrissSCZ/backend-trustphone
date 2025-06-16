from django.urls import path
from .views import main, crear_celular

urlpatterns = [
    path('', main, name='celulares'),
    path('crear_celular/', crear_celular, name='crear_celular'),
]
