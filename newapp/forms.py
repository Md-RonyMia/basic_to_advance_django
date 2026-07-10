from django import forms
from django.core import validators



def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError("Enter a vlaue with at least 10 chars")
class ContactForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput,validators=[len_check])
    email=forms.CharField(widget=forms.EmailInput)
    age=forms.IntegerField(validators=[validators.MinValueValidator(18,message='Enter a age above 18')])
    file=forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','svg'])])

        

