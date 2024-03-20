from django.urls import path
from django.contrib.auth.views import LoginView
from .views import register

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
