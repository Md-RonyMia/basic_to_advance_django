from django import forms
from django.core import validators

class ContactForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput,validators=[validators.MinLengthValidator(10,message='Enter a name with at least 10 chars')])
    email=forms.CharField(widget=forms.EmailInput)
    age=forms.IntegerField(validators=[validators.MinValueValidator(18,message='Enter a age above 18')])

        

