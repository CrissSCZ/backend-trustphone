from django.urls import path
from .views import ClienteGoogleAuthView
from .views_auth import ClienteLoginView, ClienteRegisterView
from .views import main, editar_cliente, crear_cliente
urlpatterns = [
    path('google-auth/', ClienteGoogleAuthView.as_view(), name='cliente-google-auth'),
    path('login/', ClienteLoginView.as_view(), name='cliente-login'),
    path('register/', ClienteRegisterView.as_view(), name='cliente-register'),
    path('', main , name='clientes'),
    path('editar_cliente/<uuid:id_cliente>/', editar_cliente, name='editar_cliente'),
    path('crear_cliente/', crear_cliente, name='crear_cliente'),
]
