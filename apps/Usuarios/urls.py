from django.urls import path
from .views import login, google_login, user_profile, GoogleAuthView

urlpatterns = [
    path('login/', login, name='login'),
    path('google-login/', google_login, name='google-login'),
    path('profile/', user_profile, name='profile'),
    path('google-auth/', GoogleAuthView.as_view(), name='google-auth'),
]
