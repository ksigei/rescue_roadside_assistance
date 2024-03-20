from django.urls import path
from .views import update_mechanic_profile

urlpatterns = [
    path('mechanic/update/', update_mechanic_profile, name='update_mechanic_profile'),
]