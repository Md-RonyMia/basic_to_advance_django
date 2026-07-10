from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput)
    email=forms.CharField(widget=forms.EmailInput)
    def clean_email(self):
        email=self.cleaned_data['email']
        if '.com' not in email:
            raise forms.ValidationError("Email should contain .com")
        return email
    def clean_name(self):
        name=self.cleaned_data['name']
        if len(name) < 10:
            raise forms.ValidationError("Name should be at least 10 chars")
        return name


