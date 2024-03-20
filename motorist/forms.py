from django import forms
from .models import Motorist

class MotoristProfileForm(forms.ModelForm):
    class Meta:
        model = Motorist
        fields = ['location', 'phone_number', 'profile_picture']