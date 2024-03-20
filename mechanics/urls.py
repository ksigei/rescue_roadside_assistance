from django.urls import path
from .views import mechanic_detail, mechanic_list, mechanic_profile, update_mechanic_profile

urlpatterns = [
    path('mechanics/', mechanic_list, name='mechanic_list'),
    path('mechanics/<uuid:mechanic_id>/', mechanic_detail, name='mechanic_detail'),
    path('mechanic/profile/<uuid:mechanic_id>/', mechanic_profile, name='mechanic_profile'),
    path('mechanic/update/', update_mechanic_profile, name='update_mechanic_profile'),
]