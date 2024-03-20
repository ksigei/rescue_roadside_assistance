from django.db import models
from django.contrib.auth.models import User
from mechanics.models import Mechanic
from location_field.models.plain import PlainLocationField
import uuid

class AssistanceRequest(models.Model):
    INCURRED_PROBLEM_CHOICES = [
        ('Flat Tire', 'Flat Tire'),
        ('Battery Issues', 'Battery Issues'),
        ('Engine Trouble', 'Engine Trouble'),
        ('Fuel Problem', 'Fuel Problem'),
        ('Other', 'Other'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    description = models.TextField()
    location = PlainLocationField(based_fields=['city'], zoom=7)
    is_confirmed = models.BooleanField(default=False)
    image = models.ImageField(upload_to='assistance_request_images/', null=True, blank=True)
    incurred_problem = models.CharField(max_length=50, choices=INCURRED_PROBLEM_CHOICES)

    def __str__(self):
        return f"Assistance request for {self.user} at {self.location}"

class AssistanceResponse(models.Model):
    request = models.ForeignKey(AssistanceRequest, on_delete=models.CASCADE)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    response_text = models.TextField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Response for assistance request {self.request}"
