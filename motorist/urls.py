from django.urls import path
from .views import update_motorist_profile

urlpatterns = [
    path('motorist/update/', update_motorist_profile, name='update_motorist_profile'),
]