from django import forms
from .models import Availability, CustomUser, Company
from django.contrib.auth.forms import UserCreationForm
from datetime import date


class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ['date', 'start_time', 'end_time']
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'min': date.today().isoformat()  # Set the minimum date to today
                }
            ),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email


class CompanyRegistrationForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'email', 'phone', 'website', 'description', 'logo']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }