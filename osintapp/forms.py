from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class OSINTQueryForm(forms.Form):
    phone_number = forms.CharField(max_length=15, label="Phone Number")

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']