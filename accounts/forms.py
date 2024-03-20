from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from motorist.models import Motorist
from mechanics.models import Mechanic

class CustomUserCreationForm(UserCreationForm):
    ROLE_CHOICES = (
        ('motorist', 'Motorist'),
        ('mechanic', 'Mechanic'),
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2', 'role')
