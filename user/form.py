from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'enter your name',
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'Email',
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Phone',}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
    }))
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
    }))

    class Meta:
        model = User
        fields = ['username', 'email','phone', 'password1', 'password2']