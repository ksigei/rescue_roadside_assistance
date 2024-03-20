from django.urls import path
from .views import mechanic_profile, update_mechanic_profile

urlpatterns = [
    path('mechanic/profile/<uuid:mechanic_id>/', mechanic_profile, name='mechanic_profile'),
    path('mechanic/update/', update_mechanic_profile, name='update_mechanic_profile'),
]