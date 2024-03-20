from django.db import models
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField
import uuid

class Motorist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    phone_number = models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_to='motorist_profile_pictures/', null=True, blank=True)

    def __str__(self):
        return self.user.username
