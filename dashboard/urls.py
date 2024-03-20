from django.urls import path
from . import views

urlpatterns = [
    path('mechanic/dashboard/', views.mechanic_dashboard, name='mechanic_dashboard'),
    path('motorist/dashboard/', views.motorist_dashboard, name='motorist_dashboard'),
]
