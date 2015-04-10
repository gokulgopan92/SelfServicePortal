from django.contrib.auth.models import User
from django import forms

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'