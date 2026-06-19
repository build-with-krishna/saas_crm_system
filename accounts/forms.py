from django import forms
from .models import User
from companies.models import Company


class CompanySignupForm(forms.Form):
    company_name = forms.CharField(max_length=255)
    email = forms.EmailField()
    name = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)


from django.contrib.auth.forms import AuthenticationForm
from django import forms

class LoginForm(AuthenticationForm):

    username = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control'
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        })
    )