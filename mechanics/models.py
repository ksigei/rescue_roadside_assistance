from django.db import models
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField
import uuid

class Mechanic(models.Model):
    specializations = [
        ('Flat Tire', 'Flat Tire'),
        ('Battery Issues', 'Battery Issues'),
        ('Engine Trouble', 'Engine Trouble'),
        ('Fuel Problem', 'Fuel Problem'),
        ('Other', 'Other'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specializations = models.CharField(max_length=50, choices=specializations)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to='mechanic_profile_pictures/', null=True, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

