from django import forms
from . import models

class ServiceForm(forms.ModelForm):
    class Meta:
        model = models.Service
        fields = ['name', 'description', 'duration', 'price', 'cost_price']