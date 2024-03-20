from django import forms
from .models import Mechanic

class MechanicProfileForm(forms.ModelForm):
    class Meta:
        model = Mechanic
        fields = ['location', 'phone_number', 'email', 'profile_picture']
