from django import forms
from .models import TrialRequest


class TrialForm(forms.ModelForm):
    class Meta:
        model = TrialRequest
        fields = ['full_name', 'email', 'phone']
