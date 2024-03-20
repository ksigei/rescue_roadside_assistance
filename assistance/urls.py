from django.urls import path
from . import views

urlpatterns = [
    path('request-assistance/<uuid:mechanic_id>/', views.request_assistance, name='request_assistance'),
]
