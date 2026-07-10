from django import forms
from django.core import validators


class ContactForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        self.cleaned_data=super().clean()
        val_pass=self.cleaned_data['password']
        con_pass=self.cleaned_data['confirm_password']
        name=self.cleaned_data['name']
        if val_pass!=con_pass:
            raise forms.ValidationError("Password doesn't match")
        if len(name) < 10:
            raise forms.ValidationError("Enter a name at least 10 chars")

        

