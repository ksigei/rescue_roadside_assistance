# Generated by Django 5.0.3 on 2024-03-20 08:30

import django.db.models.deletion
import location_field.models.plain
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Mechanic",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "location",
                    location_field.models.plain.PlainLocationField(max_length=63),
                ),
                ("phone_number", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254)),
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True, null=True, upload_to="mechanic_profile_pictures/"
                    ),
                ),
                ("is_available", models.BooleanField(default=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
