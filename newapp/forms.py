from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserCreate(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'id':'required'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']