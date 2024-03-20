from django.db import models
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField
import uuid

class SupportTicket(models.Model):
    NEW = 'New'
    IN_PROGRESS = 'In Progress'
    RESOLVED = 'Resolved'

    STATUS_CHOICES = (
        (NEW, 'New'),
        (IN_PROGRESS, 'In Progress'),
        (RESOLVED, 'Resolved'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=NEW)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Support ticket for {self.user} created at {self.created_at}"
