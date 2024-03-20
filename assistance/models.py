from django.db import models
from django.contrib.auth.models import User
from mechanics.models import Mechanic
from location_field.models.plain import PlainLocationField
import uuid

class AssistanceRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    description = models.TextField()
    # location = models.ForeignKey(Location, on_delete=models.CASCADE)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    is_confirmed = models.BooleanField(default=False)
    image = models.ImageField(upload_to='assistance_request_images/', null=True, blank=True)

    def __str__(self):
        return f"Assistance request for {self.user} at {self.location}"

class AssistanceResponse(models.Model):
    request = models.ForeignKey(AssistanceRequest, on_delete=models.CASCADE)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    response_text = models.TextField()
    # response_image = models.ImageField(upload_to='assistance_response_images/', null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Response for assistance request {self.request}"