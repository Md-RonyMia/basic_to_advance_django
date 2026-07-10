from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput)
    email=forms.CharField(widget=forms.EmailInput)
    def clean(self):
        self.cleaned_data=super().clean()
        name=self.cleaned_data['name']
        email=self.cleaned_data['email']
        if len(name) <10:
            raise forms.ValidationError("Name should be at least 10 chars")
        if '.com' not in email:
            raise forms.ValidationError("Email should contain .com")

        

