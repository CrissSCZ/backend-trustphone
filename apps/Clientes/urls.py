from django.urls import path
from .views import ClienteGoogleAuthView
from .views_auth import ClienteLoginView, ClienteRegisterView

urlpatterns = [
    path('google-auth/', ClienteGoogleAuthView.as_view(), name='cliente-google-auth'),
    path('login/', ClienteLoginView.as_view(), name='cliente-login'),
    path('register/', ClienteRegisterView.as_view(), name='cliente-register'),
]
