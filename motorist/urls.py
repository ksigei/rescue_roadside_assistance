from django.urls import path
from .views import motorist_profile, update_motorist_profile

urlpatterns = [
    path('motorist/<uuid:motorist_id>/', motorist_profile, name='motorist_profile'),
    path('motorist/update/', update_motorist_profile, name='update_motorist_profile'),
]

