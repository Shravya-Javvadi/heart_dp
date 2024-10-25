from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=10, required=True, min_length=10)
    dob = forms.DateField(required=True, widget=forms.SelectDateWidget(years=range(1900, 2024)))
    hospital_name = forms.CharField(required=True, max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'dob', 'hospital_name', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not re.match("^[A-Za-z0-9]*$", username):
            raise forms.ValidationError("Username must contain only letters and numbers.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if '@' not in email or '.' not in email:
            raise forms.ValidationError("Email must be a valid email address.")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if len(phone_number) != 10 or not phone_number.isdigit():
            raise forms.ValidationError("Phone number must be exactly 10 digits.")
        return phone_number

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data
