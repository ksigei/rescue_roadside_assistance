from django import forms
from .models import AssistanceRequest, AssistanceResponse

class AssistanceRequestForm(forms.ModelForm):
    class Meta:
        model = AssistanceRequest
        fields = ['incurred_problem', 'description', 'location', 'image']
        labels = {
            'incurred_problem': ' incurred_problem',
            'description': 'Description',
            'location': 'Location',
            'image': 'Image (optional)',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class AssistanceResponseForm(forms.ModelForm):
    class Meta:
        model = AssistanceResponse
        fields = ['response_text', 'is_completed']
        labels = {
            'response_text': 'Response Text',
            'is_completed': 'Is Completed',
        }
        widgets = {
            'response_text': forms.Textarea(attrs={'rows': 4}),
        }
