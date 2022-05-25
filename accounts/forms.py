from django import forms
from django.conf import settings
from . import models

class UserForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = ['number', 'birth_date']
        labels = {
            'number': 'Номер',
            'birth_date': 'Дата рождения',
        }