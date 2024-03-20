from django.urls import path
from . import views

urlpatterns = [
    path('responses/<uuid:request_id>/', views.assistance_responses, name='assistance_responses'),
    path('request-assistance/<uuid:mechanic_id>/', views.request_assistance, name='request_assistance'),
    path('respond_to_request/<uuid:request_id>/', views.respond_to_request, name='respond_to_request'),
]


