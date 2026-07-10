from django import forms

class ContactForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    age=forms.IntegerField()
    CHOICES = [('s','small'),('m','medium'),('l','large')]
    size=forms.ChoiceField(choices=CHOICES)
    MEAL = [('p','pepparoni'),('m','mashrom'),('b','beef')]
    pizaa=forms.MultipleChoiceField(choices=MEAL)